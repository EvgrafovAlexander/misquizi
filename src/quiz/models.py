# stdlib
import uuid
from datetime import datetime

# thirdparty
from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID

# project
from src.database import CustomBase


class QuizGroup(CustomBase):
    __tablename__ = "quiz_group"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, doc="Group id")
    name = Column(String(100), nullable=False, unique=True, doc="Group name")
    description = Column(String, doc="Group description")
    is_active = Column(Boolean, default=False, index=True, doc="is group active")
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
