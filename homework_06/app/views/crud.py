"""
Create
Read
Update
Delete
"""
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import db, Product, Post


def create_product(name: str) -> Product:
    product = Product(name=name)
    db.session.add(product)
    db.session.commit()
    return product


def get_products() -> list[Product]:
    # return list(Product.query.all())
    return list(db.session.scalars(select(Product)).all())


def create_post(title: str, body: str) -> Post:
    post = Post(title=title, body=body, user_id="1")
    db.session.add(post)
    db.session.commit()
    return post


def get_posts() -> list[Post]:
    # return list(Product.query.all())
    return list(db.session.scalars(select(Post)).all())