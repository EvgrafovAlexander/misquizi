# stdlib
from uuid import UUID

# thirdparty
from pydantic import BaseModel, Field


class QuizGroupAdding(BaseModel):
    """Model for adding a group of quizzes"""

    name: str = Field(title="Group name")
    description: str | None = Field(title="Group description")


class QuizAdding(BaseModel):
    """Model for adding a quiz"""

    name: str = Field(title="Quiz name")
    group_id: UUID = Field(title="Quiz group")
    description: str | None = Field(title="Quiz description")


class BaseResponse(BaseModel):
    """Base response model"""

    detail: str = "Ok"
