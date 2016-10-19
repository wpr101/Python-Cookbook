import asyncio

async def stack_printer():
	for task in asyncio.Task.all_tasks():
		task.print_stack()

loop = asyncio.get_event_loop()

result = loop.run_until_complete(stack_printer())
