import aiohttp
import asyncio
import os
import time

TARGET_URL = os.getenv("TARGET_URL", "http://51.20.96.40:5000/apidocs/")

CONCURRENT_REQUESTS = 200
TOTAL_REQUESTS = 1000

async def fetch(session, url, idx):
    try:
        async with session.get(url) as resp:
            status = resp.status
            if status != 200:
                print(f"[{idx}] Error status: {status}")
    except Exception as e:
        print(f"[{idx}] Exception: {e}")

async def run_load_test():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(TOTAL_REQUESTS):
            tasks.append(fetch(session, TARGET_URL, i))
            if len(tasks) >= CONCURRENT_REQUESTS:
                await asyncio.gather(*tasks)
                tasks = []
        if tasks:
            await asyncio.gather(*tasks)

if __name__ == "__main__":
    print(f"Starting load test to {TARGET_URL}")
    start_time = time.time()
    asyncio.run(run_load_test())
    duration = time.time() - start_time
    print(f"Finished load test in {duration:.2f} seconds")
