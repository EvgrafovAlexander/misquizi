# stdlib
import uuid
from datetime import datetime

# thirdparty
from sqlalchemy import Boolean, Column, DateTime, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

# project
from src.database import CustomBase


class QuizGroup(CustomBase):
    __tablename__ = "quiz_groups"

    id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, doc="Group id"
    )
    name = Column(String(100), nullable=False, unique=True, doc="Group name")
    description = Column(String, doc="Group description")
    is_active = Column(Boolean, default=False, index=True, doc="is group active")
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    quizzes = relationship("Quiz", back_populates="group", cascade="all, delete-orphan")


class Quiz(CustomBase):
    __tablename__ = "quizzes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, doc="Id")
    group_id = Column(UUID(as_uuid=True), ForeignKey("quiz_groups.id"), index=True)
    name = Column(String(100), nullable=False, unique=True, doc="Quiz name")
    description = Column(String, doc="Quiz description")
    is_active = Column(Boolean, default=False, index=True, doc="is quiz active")
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    group = relationship("QuizGroup", back_populates="quizzes")
