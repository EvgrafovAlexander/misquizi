# stdlib
from http import HTTPStatus

# thirdparty
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

# project
from logger import logger
from src.quiz.repositories.quiz_group import QuizGroupRepository
from src.quiz.schemas import QuizGroupAdding
from src.utils.controller import AsyncController


class AddQuizGroupController(AsyncController):
    def __init__(self, quiz_group: QuizGroupAdding, session: AsyncSession):
        self.quiz_group = quiz_group
        self.session = session

    async def __call__(self, *args, **kwargs) -> dict:
        try:
            logger.info("AddQuizGroupController, quiz_group: %s" % self.quiz_group.name)
            id = await QuizGroupRepository(session=self.session).add_quiz_group(
                self.quiz_group
            )
            return {"id": id}
        except Exception as e:
            logger.error("AddQuizGroupController Error, detail: %s" % e)
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail=f"AddQuizGroupController Error, detail: {e}",
            )
