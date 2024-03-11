"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


import asyncio
import logging

from aiohttp import ClientSession
from sqlalchemy import select
import common

log = logging.getLogger(__name__)


async def fetch_json(url: str) -> dict:
    async with ClientSession() as session:
        async with session.get(url) as response:
            data: dict = await response.json()
            return data


async def fetch_users_data():
    common.configure_logging()
    log.info("fetch_users_data")
    users_data = await fetch_json(USERS_DATA_URL)
 #   log.info("users_data json: %s", users_data)
    return users_data


async def fetch_posts_data():
    common.configure_logging()
    log.info("fetch_posts_data")
    posts_data = await fetch_json(POSTS_DATA_URL)
#    log.info("posts_data json: %s", posts_data)
    return posts_data


if __name__ == "__main__":
    asyncio.run(fetch_users_data())
    asyncio.run(fetch_posts_data())
