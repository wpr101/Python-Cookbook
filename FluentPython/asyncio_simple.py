import asyncio
def run_sync(coro_or_future):
	loop = asyncio.get_event_loop()
	return loop.run_until_complete(coro_or_future)

a = run_sync(some_coroutine())
