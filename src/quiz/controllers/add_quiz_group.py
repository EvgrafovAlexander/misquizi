# thirdparty
from sqlalchemy.ext.asyncio import AsyncSession

# project
from src.quiz.repositories.quiz_groups import QuizGroupsRepository
from src.quiz.schemas import QuizGroupAdding, BaseResponse
from src.utils.controller import AsyncController


class AddQuizGroupController(AsyncController):
    def __init__(self, quiz_group: QuizGroupAdding, session: AsyncSession):
        self.quiz_group = quiz_group
        self.session = session

    async def __call__(self, *args, **kwargs) -> BaseResponse:
        await QuizGroupsRepository(session=self.session).add_quiz_group(self.quiz_group)
        return BaseResponse()
