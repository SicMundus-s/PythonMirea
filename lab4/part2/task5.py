import asyncio

async def print_numbers():
    for i in range(1, 6):
        print(i)
        await asyncio.sleep(1)

async def main():
    await asyncio.gather(print_numbers(), print_numbers(), print_numbers())

asyncio.run(main())