# project
from src.quiz.models import QuizGroup
from src.quiz.schemas import QuizGroupAdding
from src.utils.repository import BaseRepository


class QuizGroupRepository(BaseRepository):
    model = QuizGroup

    async def add_quiz_group(self, quiz_group: QuizGroupAdding):
        async with self.session.begin():
            quiz_group = self._create_alchemy_model(quiz_group)
            self.session.add(quiz_group)
            await self._commit()
