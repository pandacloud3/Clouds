import aiohttp
import asyncio
import time
import os

TARGET_URL = os.getenv("TARGET_URL", "http://51.20.96.40:5000/apidocs/")
NUM_REQUESTS = 5000
CONCURRENCY = 100  

async def make_request(session, sem):
    async with sem:
        try:
            async with session.get(TARGET_URL) as resp:
                await resp.text()
        except Exception as e:
            print(f"Request failed: {e}")

async def stress_test():
    sem = asyncio.Semaphore(CONCURRENCY)
    async with aiohttp.ClientSession() as session:
        tasks = [make_request(session, sem) for _ in range(NUM_REQUESTS)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    print(f"Starting load test to {TARGET_URL}")
    start = time.time()
    asyncio.run(stress_test())
    print(f"Finished load test in {time.time() - start:.2f}s")
