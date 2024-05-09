# stdlib
from collections.abc import AsyncGenerator

# thirdparty
from sqlalchemy import exc
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.ext.declarative import declarative_base

# project
from src.config import db_config


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    engine = create_async_engine(db_config.url)
    factory = async_sessionmaker(engine)
    async with factory() as session:
        try:
            yield session
            await session.commit()
        except exc.SQLAlchemyError as e:
            await session.rollback()
            raise


# Model base class
Base = declarative_base()
