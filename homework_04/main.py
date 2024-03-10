"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- 
            - загрузка пользователей и постов должна выполняться конкурентно (параллельно) 
              при помощи [`asyncio.gather`](https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
            - функции должны создавать новые объекты (например списки со словарями) и возвращать их как результат. 
              Например:
              ```python
              users_data: List[dict]
              posts_data: List[dict]
              users_data, posts_data = await asyncio.gather(
                  fetch_users_data(),
                  fetch_posts_data(),
              )
              ```
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio
from typing import Sequence

from sqlalchemy import select, update
from sqlalchemy import and_
from sqlalchemy import func
from sqlalchemy import or_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session, defer
from sqlalchemy.orm import joinedload
from sqlalchemy.orm import selectinload

from jsonplaceholder_requests import return_data

from models import User, Post
from models import Session


async def create_user(
    session: AsyncSession,
    name: str,
    username: str,
    email: str | None = None,
) -> User:
    user = User(
        name=name,
        username=username,
        email=email,
    )
    session.add(user)
    await session.commit()

    print("saved user")
    print("user info:", user)
    # session.refresh(user)

    return user

async def create_posts(
    session: AsyncSession,
    user: User,
    *posts_titles: str,
) -> list[Post]:
    posts = [
        # create a new post for this user
        Post(title=title, user_id=user.id)
        # for each title in titles
        for title in posts_titles
    ]
    session.add_all(posts)
    await session.commit()

    for post in posts:
        print(post)

    print(posts)

    return posts

async def async_main():
    async with Session() as session:
      user: User = await create_user(
        session,
        "john",
        "john snow",
        "john@bg.com"
    )
    # users_data = await return_data()
    # result = [{'name': user['name'], 'username': user['username']} for user in users_data]
    # print(repr(result))
    # async with Session() as session:
    #     for user in users_data:
    #       user: User = await create_user(
    #           session,
    #           name=user['name'],
    #           username=user['username'],
    #           email=user['email']
            
    #     ) 
        
        


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
