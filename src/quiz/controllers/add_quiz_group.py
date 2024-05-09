# thirdparty
from sqlalchemy.ext.asyncio import AsyncSession

# project
from src.quiz.repositories.quiz_group import QuizGroupRepository
from src.quiz.schemas import QuizGroupAdding
from src.utils.controller import AsyncController


class AddQuizGroupController(AsyncController):
    def __init__(self, quiz_group: QuizGroupAdding, session: AsyncSession):
        self.quiz_group = quiz_group
        self.session = session

    async def __call__(self, *args, **kwargs):
        return await QuizGroupRepository(session=self.session).add_quiz_group(self.quiz_group)
