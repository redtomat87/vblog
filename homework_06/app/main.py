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
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from jsonplaceholder_requests import fetch_users_data, fetch_posts_data

from models import User
from models import Post
from models import Session
from alembic.config import Config
from alembic import command

alembic_cfg = Config("alembic.ini")
command.upgrade(alembic_cfg, "head")


async def create_users(
    session: AsyncSession,
    *users_data
) -> list[User]:
    
    users = []
    for user_data in users_data:
        user = User(
            name=user_data['name'],
            username=user_data['username'],
            email=user_data['email']
        )
        users.append(user)

    session.add_all(users)
    await session.commit()

    return users


async def create_posts(
    session: AsyncSession,
    *posts_data
) -> list[Post]:
    
    posts = []                                 
    for post in posts_data:
        post = Post(
            title = post['title'],
            body = post['body'],
            user_id = post['userId']            
        )
        posts.append(post)

    session.add_all(posts)
    await session.commit()

    return posts


async def async_main():

    async with Session() as session:
        
        users_data, posts_data = await asyncio.gather(
            fetch_users_data(),
            fetch_posts_data(),
        )

        await create_users(session, *users_data)
        await create_posts(session, *posts_data)
            
      
def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
