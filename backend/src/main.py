import uvicorn
from fastapi import Query, Depends, FastAPI, HTTPException
from fastapi.responses import ORJSONResponse
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from db import get_session
from models import Student, StudentCreate, StudentRead
from models import Major, MajorCreate, MajorRead


app = FastAPI(
    title='MODEUS',
    description='Yet Another Modeus Realisation',
    version='2.0',
    openapi_url='/docs/openapi.json',
    default_response_class=ORJSONResponse,
    docs_url='/docs',
    redoc_url=None,
)


@app.get('/api/v1/sus', response_model=dict[str, str])
async def sas(session: AsyncSession = Depends(get_session)) -> dict[str, str]:
    major = await session.exec(select(Major).where(Major.eng_name == 'IT'))
    if major.first():
        return {'sus': 'sas'}
    major = Major(eng_name='IT', ru_name='ОЙТИ', fgos_name='Информационные технологии')
    session.add(major)
    await session.commit()

    return {'sas': 'sus'}


@app.patch('/api/v1/student/{student_id}', response_model=StudentRead)
async def year_student(student_id: int, year: int, session: AsyncSession = Depends(get_session)) -> StudentRead:
    student = await session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail='Student not found')
    student.year = year
    await session.commit()
    print(student)
    return student


@app.get('/api/v1/student/{student_id}', response_model=StudentRead)
async def get_student(student_id: int, session: AsyncSession = Depends(get_session)) -> StudentRead:
    student = await session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail='Student not found')
    return student


@app.get('/api/v1/students', response_model=list[StudentRead])
async def get_students(
        offset: int = 0, limit: int = Query(default=100, lte=100),
        session: AsyncSession = Depends(get_session)) -> list[StudentRead]:
    result = await session.exec(select(Student).offset(offset).limit(limit))
    return result.all()


@app.post('/api/v1/student', response_model=StudentRead)
async def add_student(student: StudentCreate, session: AsyncSession = Depends(get_session)) -> StudentRead:
    student = Student.from_orm(student)
    session.add(student)
    await session.commit()
    # Seems, that refreshing is not necessary
    # await session.refresh(student)
    return student


@app.post('/api/v1/major', response_model=MajorRead)
async def add_major(major: MajorCreate, session: AsyncSession = Depends(get_session)) -> MajorRead:
    major = Major.from_orm(major)
    session.add(major)
    await session.commit()
    return major


# @app.post('/api/v1/course', response_model=Course)
# async def add_course(course: Course, session: AsyncSession = Depends(get_session)) -> Course:
#     course = Course(**course.dict())
#     session.add(course)
#     await course.commit()
#     return course


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', reload=True)  # , log_level='critical')
