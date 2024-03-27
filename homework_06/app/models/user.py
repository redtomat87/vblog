# from typing import TYPE_CHECKING
#
from sqlalchemy import Column
from sqlalchemy import String

from sqlalchemy.orm import relationship

from models.db import db
from models.mixins.created_at_mixin import CreatedAtMixin
from models.base import Base

class User(CreatedAtMixin, db.Model):

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


