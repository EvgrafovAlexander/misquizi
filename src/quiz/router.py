# thirdparty
from fastapi import APIRouter

# project
from src.quiz.controllers.add_quiz_group import AddQuizGroupController
from src.quiz.schemas import QuizGroupAdding


router = APIRouter(prefix="/quiz", tags=["quiz"])


@router.post("/group/add")
async def add_quiz_group(group: QuizGroupAdding):
    """Adding a new group of quizzes"""
    return await AddQuizGroupController(group)()
