# thirdparty
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

# project
from src.database import get_db_session
from src.quiz.controllers.add_quiz import AddQuizController
from src.quiz.controllers.add_quiz_group import AddQuizGroupController
from src.quiz.schemas import BaseResponse, QuizAdding, QuizGroupAdding


router = APIRouter(prefix="/quiz", tags=["quiz"])


@router.post("/group/add", response_model=BaseResponse)
async def add_quiz_group(
    group: QuizGroupAdding,
    session: AsyncSession = Depends(get_db_session),
):
    """Adding a new group of quizzes"""
    return await AddQuizGroupController(group, session)()


@router.post("/add", response_model=BaseResponse)
async def add_quiz(
    quiz: QuizAdding,
    session: AsyncSession = Depends(get_db_session),
):
    """Adding a new quiz"""
    return await AddQuizController(quiz, session)()
