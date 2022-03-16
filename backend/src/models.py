from enum import Enum
from typing import List, Optional

from sqlmodel import SQLModel, Field, Relationship


__all__ = [
    'Student', 'Major',
    'Course', 'CourseMajorLink',
    'Enrollment',
    # 'Grade', 'FacultyMember', 'Minor', 'Attendance',
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
# A: It could be None when just created and doesn't exist in db
class CourseMajorLink(SQLModel, table=True):
    course_id: int | None = Field(
        default=None, foreign_key="course.id", primary_key=True, nullable=False
    )
    major_id: int | None = Field(
        default=None, foreign_key="major.id", primary_key=True, nullable=False
    )


# class Attendance(SQLModel, table=True):
#     enrollment_id: int | None = Field(
#         default=None, foreign_key="enrollment.id", primary_key=True, nullable=False
#     )
#     class_id: int | None = Field(
#         default=None, foreign_key="class.id", primary_key=True, nullable=False
#     )
#     status: str


class Enrollment(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, nullable=False)
    course_id: int | None = Field(
        default=None, foreign_key="course.id"
    )
    student_id: int | None = Field(
        default=None, foreign_key="student.id"
    )

    # classes: List["Class"] = Relationship(back_populates="enrollments", link_model=Attendance)


# class Grade(SQLModel, table=True):
#     student_id: int | None = Field(
#         default=None, foreign_key="student.id", primary_key=True, nullable=False
#     )
#     assignment_id: int | None = Field(
#         default=None, foreign_key="assignment.id", primary_key=True, nullable=False
#     )
#     value: float


class StudentBase(SQLModel):
    name: str = Field(index=True)
    year: int

    major_id: int | None = Field(default=None, foreign_key="major.id")


class Student(StudentBase, table=True):
    id: int | None = Field(default=None, primary_key=True, nullable=False)

    courses: List["Course"] = Relationship(back_populates="students", link_model=Enrollment)
    major: Optional["Major"] = Relationship(back_populates="students")


class StudentCreate(StudentBase):
    pass


class StudentRead(StudentBase):
    id: int


class StudentReadWithLinks(StudentRead):
    courses: List["CourseRead"] = []
    major: Optional["MajorRead"] = None


# class FacultyMember(SQLModel):
#     id: int | None = Field(default=None, primary_key=True, nullable=False)
#     name: str
#     name_rus: str
#     mail: str
#     status: str


# class VisitingFaculty(FacultyMember, table=True):
#     pass


# class PermanentFaculty(FacultyMember, table=True):
#     pass


class CourseBase(SQLModel):
    name: str
    hours: int
    assessment_type: str
    course_type: CourseType
    course_weight: float
    module: str
    start_date: str
    end_date: str
    exam_date: str
    status: CourseStatus


class Course(CourseBase, table=True):
    id: int | None = Field(default=None, primary_key=True, nullable=False)

    students: List[Student] = Relationship(back_populates="courses", link_model=Enrollment)
    # assignments: List["Assignment"] = Relationship(back_populates="course")
    # classes: List["Class"]  = Relationship(back_populates="course")
    majors: List["Major"] = Relationship(back_populates="courses", link_model=CourseMajorLink)
    # minors: List["Minor"] = Relationship(back_populates="course")  # ??? , link_model=CourseMinorLink)


class CourseCreate(CourseBase):
    pass


class CourseRead(CourseBase):
    id: int


class CourseReadWithLinks(CourseRead):
    students: List[StudentRead] = []
    majors: List["MajorRead"] = []


# class MinorBase(SQLModel):
#     eng_name: str
#     ru_name: str
#     fgos_name: str


# class Minor(MinorBase, table=True):
#     id: int | None = Field(default=None, primary_key=True, nullable=False)

#     course_id: int | None = Field(default=None, foreign_key="course.id")
#     courses: List[Course] = Relationship(back_populates="minors")  # ??? , link_model=CourseMinorLink)


# class AssignmentBase(SQLModel):
#     id: int | None = Field(default=None, primary_key=True, nullable=False)
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
#     id: int | None = Field(default=None, primary_key=True, nullable=False)
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
    id: int | None = Field(default=None, primary_key=True, nullable=False)

    students: List[Student] = Relationship(back_populates="major")
    courses: List[Course] = Relationship(back_populates="majors", link_model=CourseMajorLink)


class MajorCreate(MajorBase):
    pass


class MajorRead(MajorBase):
    id: int


class MajorReadWithLinks(MajorRead):
    students: List[StudentRead] = []
    courses: List[CourseRead] = []


# class FinalGrade(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True, nullable=False)
#     value: float


# TODO: Why?
CourseReadWithLinks.update_forward_refs()
StudentReadWithLinks.update_forward_refs()
