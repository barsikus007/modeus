from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship
from enum import Enum

# TODO: Find a way to define these enums for fields
class StudentStatus(Enum):
    ACTIVE = 'active'
    ON_LEAVE = 'on_leave'
    TRANSFERED = 'transferred'
    EXPELLED = 'expelled'

class CourseType(Enum):
    ELECTIVE = 'elective'
    MAJOR = 'major'
    CORE = 'core'

class CourseGradingType(Enum):
    PASS_FAIL = 'pass_fail'
    MEDIAN = 'median'
    AVERAGE = 'average'
    GRADE = 'grade'

class CourseStatus(Enum):
    ARCHIVED = 'archived'
    ACTIVE = 'active'
    DRAFT = 'draft'


__all__ = ['Student']




# FIXME: Should the *_id types be optional for a surrogate table?

class CourseMajorLink(SQLModel, table=True):
    course_id: Optional[int] = Field(
        default=None, foreign_key="course.id", primary_key=True
    )
    major_id: Optional[int] = Field(
        default=None, foreign_key="major.id", primary_key=True
    )
    status: str


class Attendance(SQLModel, table=True):
    enrolled_id: Optional[int] = Field(
        default=None, foreign_key="enrollment.id", primary_key=True
    )
    class_id: Optional[int] = Field(
        default=None, foreign_key="student.id", primary_key=True
    )
    status: str


class Enrollment(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    course_id: Optional[int] = Field(
        default=None, foreign_key="course.id", primary_key=True
    )
    student_id: Optional[int] = Field(
        default=None, foreign_key="student.id", primary_key=True
    )

    classes: List["Class"] = Relationship(back_populates="enrollments", link_model=Attendance)
    

class Grade(SQLModel, table=True):
    student_id: Optional[int] = Field(
        default=None, foreign_key="enrolled.id", primary_key=True
    )
    assignment_id: Optional[int] = Field(
        default=None, foreign_key="student.id", primary_key=True
    )
    value: float


class StudentBase(SQLModel):
    name: str = Field(index=True)
    year: int
    major: str


class Student(StudentBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    course_id: Optional[int] = Field(default=None, foreign_key="course.id")
    courses: List["Course"] = Relationship(back_populates="student", link_model=Enrollment)
    major: "Major" = Relationship(back_populates="students")

class StudentCreate(StudentBase):
    pass


class StudentRead(StudentBase):
    id: int


class FacultyMember(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    name_rus: str
    mail: str
    status: str


class VisitingFaculty(FacultyMember, table=True):
    pass


class PermanentFaculty(FacultyMember, table=True):
    pass


class Course(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    hours: int
    assessment_type: str 
    course_type: str 
    course_weight: float
    module: str
    start_date: str
    end_date: str 
    exam_date: str
    status: str

    students: List[Student] | None = Relationship(default=None, back_populates="course", link_model=Enrollment) 
    assignments: List["Assignment"] | None = Relationship(default=None, back_populates="course")
    classes: List["Class"] | None  = Relationship(default=None, back_populates="course") 
    minors: List["Minor"] | None = Relationship(default=None, back_populates="course")
    majors: List["Major"] | None = Relationship(default=None, back_populates="courses", link_model=CourseMajorLink)

class Minor(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    eng_name: str
    ru_name: str
    fgos_name: str

    course_id: Optional[int] = Field(default=None, foreign_key="course.id")
    courses: List["Course"] | None = Relationship(default=None, back_populates="minors")


class Assignment(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    pass_type: str
    weight: float
    name: str

    course_id: int = Field(default=None, foreign_key="course.id")
    course: Course = Relationship(back_populates="assignments")


class MakeUp(Assignment, table=True):
    is_pass: bool 
    weight: float | None = Field(default=None)

class Class(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    type: str
    week: int
    descr: str

    course_id: int = Field(default=None, foreign_key="course.id")
    course: Course = Relationship(back_populates="classes")
    enrollments: List[Enrollment] | None = Relationship(default=None, back_populates="classes", link_model=Attendance)
    

class Major(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    eng_name: str
    ru_name: str
    fgos_name: str

    students: List[Student] | None = Relationship(default=None, back_populates="major")
    courses: List[Course] | None = Relationship(default=None, back_populates="major", link_model=CourseMajorLink)

class FinalGrade(SQLModel, table=True):
    value: float