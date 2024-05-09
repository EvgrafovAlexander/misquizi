# stdlib
from http import HTTPStatus

# thirdparty
from fastapi import HTTPException

# project
from src.quiz.models import QuizGroup
from src.quiz.schemas import QuizGroupAdding
from src.utils.repository import BaseRepository


class QuizGroupRepository(BaseRepository):
    model = QuizGroup

    def _create_quiz_group_model(self, quiz_group: QuizGroupAdding):
        return self.model(
            name=quiz_group.name,
            description=quiz_group.description,
        )

    async def add_quiz_group(self, quiz_group: QuizGroupAdding):
        try:
            quiz_group = self._create_quiz_group_model(quiz_group)
            self.session.add(quiz_group)
            await self.session.commit()
        except Exception as e:
            await self.session.rollback()
            raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR, detail=f"DB Add quiz group error: {e}")
