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



async def return_data():
    common.configure_logging()
    log.info("Starting step 7")
    users_data = await fetch_json(USERS_DATA_URL)
 #   log.info("users_data json: %s", users_data)
 #   posts_data = await fetch_json(POSTS_DATA_URL)
 #   log.info("posts_data json: %s", posts_data)
    return users_data #posts_data


if __name__ == "__main__":
    asyncio.run(return_data())
