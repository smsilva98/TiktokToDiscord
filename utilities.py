import asyncio
from functools import wraps, partial
from typing import TypeVar, Callable, Awaitable

T = TypeVar('T')


def sync_to_async(func: Callable[..., T]) -> Callable[..., Awaitable[T]]:
    @wraps(func)
    async def run(*args, loop=None, executor=None, **kwargs) -> T:
        if loop is None:
            loop = asyncio.get_event_loop()
        pfunc = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, pfunc)
    return run
