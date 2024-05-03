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


from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)


PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+psycopg://user:example@localhost:5432/blog"


async_engine = create_async_engine(
    PG_CONN_URI,
    echo=True,
)


Session = async_sessionmaker(
    bind=async_engine,
    autocommit=False,
    expire_on_commit=False,
)