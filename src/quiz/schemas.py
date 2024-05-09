# thirdparty
from pydantic import BaseModel, Field


class QuizGroupAdding(BaseModel):
    """Model for adding a group of quizzes"""

    name: str = Field(title="Group name")
    description: str | None = Field(title="Group description")


class BaseResponse(BaseModel):
    """Base response model"""

    detail: str = "Ok"
