# project
from src.quiz.schemas import QuizGroupAdding
from src.utils.controller import AsyncController


class AddQuizGroupController(AsyncController):
    def __init__(self, quiz_group: QuizGroupAdding):
        self.quiz_group = quiz_group

    async def __call__(self, *args, **kwargs):
        pass
