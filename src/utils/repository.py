# thirdparty
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

# project
from src.database import Base


class BaseRepository:
    model = Base

    def __init__(self, session: AsyncSession):
        self.session = session

    def _create_alchemy_model(self, pydantic_model: BaseModel):
        return self.model(**pydantic_model.dict())
