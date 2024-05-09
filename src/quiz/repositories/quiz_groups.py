# stdlib
from http import HTTPStatus

# thirdparty
from fastapi import HTTPException

# project
from src.quiz.models import QuizGroups
from src.quiz.schemas import QuizGroupAdding
from src.utils.repository import BaseRepository


class QuizGroupsRepository(BaseRepository):
    model = QuizGroups

    async def add_quiz_group(self, quiz_group: QuizGroupAdding):
        try:
            quiz_group = self._create_alchemy_model(quiz_group)
            self.session.add(quiz_group)
            await self.session.commit()
        except Exception as e:
            await self.session.rollback()
            raise HTTPException(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                detail=f"DB Add quiz group error: {e}",
            )
