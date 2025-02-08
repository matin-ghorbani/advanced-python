import asyncio
from random import randint
from time import perf_counter

import requests_utils as ru


async def get_movie_async(movie_id: int) -> dict:
    url = f'https://imdb.iamidiotareyoutoo.com/search?tt={movie_id}'
    return await ru.get_http(url)


def get_movie_sync(movie_id: int) -> dict:
    url = f'https://imdb.iamidiotareyoutoo.com/search?tt={movie_id}'
    return ru.get_http_sync(url)


async def main() -> None:
    # Sync test
    time_begin = perf_counter()
    movie_id = 3
    for _ in range(30):
        get_movie_sync(movie_id)
    print(f'Total time for sync: {perf_counter() - time_begin}')

    # Async test
    time_begin = perf_counter()
    await asyncio.gather(*[get_movie_async(movie_id) for _ in range(30)])
    print(f'Total time for async: {perf_counter() - time_begin}')

if __name__ == '__main__':
    asyncio.run(main=main())
