# stdlib
from http import HTTPStatus

# thirdparty
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

# project
from logger import logger
from src.quiz.repositories.quiz import QuizRepository
from src.quiz.schemas import QuizAdding, BaseResponse
from src.utils.controller import AsyncController


class AddQuizController(AsyncController):
    def __init__(self, quiz: QuizAdding, session: AsyncSession):
        self.quiz = quiz
        self.session = session

    async def __call__(self, *args, **kwargs) -> BaseResponse:
        try:
            logger.info("AddQuizController, quiz: %s" % self.quiz.name)
            await QuizRepository(session=self.session).add_quiz(self.quiz)
            return BaseResponse()
        except Exception as e:
            logger.error("AddQuizController Error, detail: %s" % e)
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail=f"AddQuizController Error, detail: {e}",
            )
