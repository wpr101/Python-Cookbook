import asyncio

async def sleeper(delay):
	await asyncio.sleep(delay)
	print('Finished sleeper with delay: %d' % delay)

# Create the event loop
loop = asyncio.get_event_loop()

# Create the task
result = loop.call_soon(loop.create_task, sleeper(1))

# Make sure the loop stops after 2 seconds
result = loop.call_later(2, loop.stop)

# Start the loop and make it run forever. Or at least until the loop.stop gets 
# called in 2 seconds
loop.run_forever()
