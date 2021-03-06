import asyncio

async def main():
    for ch in "Hello, World!":
        print(ch, end="", flush=True)
        await asyncio.sleep(.005)
    print()

if __name__ == "__main__":
    asyncio.run(main())
