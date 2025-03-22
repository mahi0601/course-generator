from pydantic import BaseModel
from typing import List

class CourseRequest(BaseModel):
    brief: str
    target_audience: str

class Lesson(BaseModel):
    title: str
    content: str
    resources: List[str] = []

class Module(BaseModel):
    title: str
    lessons: List[Lesson]

class CourseResponse(BaseModel):
    course_title: str
    description: str
    modules: List[Module]
    references: List[str]
