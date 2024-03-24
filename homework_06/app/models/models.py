"""
!создайте алхимичный engine
! добавьте declarative base (свяжите с engine)
! создайте объект Session
! добавьте модели User и Post, объявите поля:
! для модели User обязательными являются name, username, email
! для модели Post обязательными являются user_id, title, body
! создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from datetime import datetime

from sqlalchemy.orm import relationship

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import func
from sqlalchemy import ForeignKey

from .mixins.created_at_mixin import CreatedAtMixin
from .base import Base

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)


PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://user:example@localhost:5432/blog"

async_engine = create_async_engine(
    PG_CONN_URI,
    echo=True,
)


Session = async_sessionmaker(
    bind=async_engine,
    autocommit=False,
    expire_on_commit=False,
)


class User(CreatedAtMixin, Base):

    name = Column(String(32), nullable=False, unique=True)
    email = Column(String, nullable=True, unique=False)
    username = Column(String(50), nullable=True, index=True)

    posts = relationship(
        # accessed through `Post.author`
        "Post",
        back_populates="user",
        uselist=True,
        # cascade="all, delete-orphan",
    )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            "User("
            f"id={self.id}"
            f", username={self.username!r}"
            f", email={self.email!r}"
            f", name={self.name!r}"
            ")"
        )


class Post(CreatedAtMixin, Base):
    title = Column(
        String(100),
        nullable=False,
        default="",
        server_default="",
    )
    body = Column(Text, nullable=False, default="", server_default="",)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=False,
        nullable=False,
    )

    published_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        server_default=func.now(),
    )

    user = relationship(
        # accessed through `User.posts`
        "User",
        back_populates="posts",
        uselist=False,
    )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"Post(id={self.id}, "
            f"title={self.title!r}, "
            f"published_at={self.published_at!r}, "
            f"user_id={self.user_id})"
        )