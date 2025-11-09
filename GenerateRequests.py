import asyncio
import aiohttp
import time

URL = "http://51.20.96.40:5000/apidocs/"

NUM_REQUESTS = 5000
CONCURRENT_REQUESTS = 200

async def send_request(session, i):
    try:
        async with session.get(URL) as response:
            status = response.status
            print(f"Request {i}: {status}")
    except Exception as e:
        print(f"Request {i} failed: {e}")

async def main():
    semaphore = asyncio.Semaphore(CONCURRENT_REQUESTS)

    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(NUM_REQUESTS):

            async with semaphore:
                tasks.append(asyncio.create_task(send_request(session, i)))

        await asyncio.gather(*tasks)

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    print(f"Completed in {time.time() - start_time:.2f} seconds")
