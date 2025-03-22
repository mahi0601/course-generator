from fastapi import FastAPI
from models import CourseRequest, CourseResponse
from core.agent_orchestrator import generate_complete_course

app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Welcome to Course Generator API. Use /docs to test the API."}

@app.post("/generate_course", response_model=CourseResponse)
def generate_course(request: CourseRequest):
    course = generate_complete_course(request.brief, request.target_audience)
    return course
