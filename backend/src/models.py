from enum import Enum
from typing import List, Optional

from sqlmodel import SQLModel, Field, Relationship


__all__ = [
    'Student', 'Major',
    # 'CourseMajorLink', 'Attendance',
    # 'Enrollment', 'Grade', 'FacultyMember', 'Course', 'Minor',
    # 'Assignment', 'MakeUp', 'Class',
]


# TODO: Find a way to define these enums for fields
# TODO: add sqlaclhemy enums https://github.com/tiangolo/sqlmodel/pull/24
class StudentStatus(str, Enum):
    ACTIVE = 'active'
    ON_LEAVE = 'on_leave'
    TRANSFERED = 'transferred'
    EXPELLED = 'expelled'

class CourseType(str, Enum):
    ELECTIVE = 'elective'
    MAJOR = 'major'
    CORE = 'core'

class CourseGradingType(str, Enum):
    PASS_FAIL = 'pass_fail'
    MEDIAN = 'median'
    AVERAGE = 'average'
    GRADE = 'grade'

class CourseStatus(str, Enum):
    ARCHIVED = 'archived'
    ACTIVE = 'active'
    DRAFT = 'draft'


# FIXME: Should the *_id types be optional for a surrogate table?

# class CourseMajorLink(SQLModel, table=True):
#     course_id: int | None = Field(
#         default=None, foreign_key="course.id", primary_key=True
#     )
#     major_id: int | None = Field(
#         default=None, foreign_key="major.id", primary_key=True
#     )


# class Attendance(SQLModel, table=True):
#     enrollment_id: int | None = Field(
#         default=None, foreign_key="enrollment.id", primary_key=True
#     )
#     class_id: int | None = Field(
#         default=None, foreign_key="class.id", primary_key=True
#     )
#     status: str


# class Enrollment(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     course_id: int | None = Field(
#         default=None, foreign_key="course.id"
#     )
#     student_id: int | None = Field(
#         default=None, foreign_key="student.id"
#     )

#     classes: List["Class"] = Relationship(back_populates="enrollments", link_model=Attendance)


# class Grade(SQLModel, table=True):
#     student_id: int | None = Field(
#         default=None, foreign_key="student.id", primary_key=True
#     )
#     assignment_id: int | None = Field(
#         default=None, foreign_key="assignment.id", primary_key=True
#     )
#     value: float


class StudentBase(SQLModel):
    name: str = Field(index=True)
    year: int

    major_id: int | None = Field(default=None, foreign_key="major.id")


class Student(StudentBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    # courses: List["Course"] = Relationship(back_populates="student", link_model=Enrollment)
    major: Optional["Major"] = Relationship(back_populates="students")


class StudentCreate(StudentBase):
    pass


class StudentRead(StudentBase):
    id: int


# class FacultyMember(SQLModel):
#     id: int | None = Field(default=None, primary_key=True)
#     name: str
#     name_rus: str
#     mail: str
#     status: str


# class VisitingFaculty(FacultyMember, table=True):
#     pass


# class PermanentFaculty(FacultyMember, table=True):
#     pass


# class Course(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     name: str
#     hours: int
#     assessment_type: str
#     course_type: CourseType
#     course_weight: float
#     module: str
#     start_date: str
#     end_date: str
#     exam_date: str
#     status: CourseStatus

#     students: List[Student] | None = Relationship(back_populates="course", link_model=Enrollment)
#     assignments: List["Assignment"] | None = Relationship(back_populates="course")
#     classes: List["Class"] | None  = Relationship(back_populates="course")
#     minors: List["Minor"] | None = Relationship(back_populates="course")
#     majors: List["Major"] | None = Relationship(back_populates="courses", link_model=CourseMajorLink)

# class Minor(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     eng_name: str
#     ru_name: str
#     fgos_name: str

#     course_id: int | None = Field(default=None, foreign_key="course.id")
#     courses: List[Course] | None = Relationship(back_populates="minors")


# class AssignmentBase(SQLModel):
#     id: int | None = Field(default=None, primary_key=True)
#     pass_type: str
#     weight: float
#     name: str

#     course_id: int = Field(default=None, foreign_key="course.id")
#     course: Course = Relationship(back_populates="assignments")


# class Assignment(AssignmentBase, table=True):
#     pass


# class MakeUp(AssignmentBase, table=True):
#     is_pass: bool
#     weight: float | None = Field(default=None)


# class Class(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     type: str
#     week: int
#     descr: str

#     course_id: int = Field(default=None, foreign_key="course.id")
#     course: Course = Relationship(back_populates="classes")
#     enrollments: List[Enrollment] | None = Relationship(back_populates="classes", link_model=Attendance)


class MajorBase(SQLModel):
    eng_name: str
    ru_name: str
    fgos_name: str


class Major(MajorBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    students: list[Student] = Relationship(back_populates="major")
    # courses: List[Course] | None = Relationship(back_populates="major", link_model=CourseMajorLink)


class MajorCreate(MajorBase):
    pass


class MajorRead(MajorBase):
    id: int

# class FinalGrade(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     value: float
