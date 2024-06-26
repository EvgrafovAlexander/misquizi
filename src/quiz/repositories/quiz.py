# stdlib
from uuid import UUID

# project
from src.quiz.models import Quiz
from src.quiz.schemas import QuizAdding
from src.utils.repository import BaseRepository


class QuizRepository(BaseRepository):
    model = Quiz

    async def add_quiz(self, quiz: QuizAdding) -> UUID:
        async with self.session.begin():
            quiz = self._create_alchemy_model(quiz)
            self.session.add(quiz)
            await self._commit()
        await self.session.refresh(quiz)
        return quiz.id
