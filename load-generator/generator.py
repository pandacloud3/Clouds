import requests
import threading
import time
import os

TARGET_URL = os.getenv("TARGET_URL", "http://51.20.96.40:5000/apidocs/")

NUM_THREADS = 700
REQUESTS_PER_THREAD = 50

def worker(thread_id):
    for _ in range(REQUESTS_PER_THREAD):
        try:
            response = requests.get(TARGET_URL)
            if response.status_code != 200:
                print(f"[{thread_id}] Error: {response.status_code}")
        except Exception as e:
            print(f"[{thread_id}] Exception: {e}")
        time.sleep(0.05)

if __name__ == "__main__":
    print(f"Starting load test to {TARGET_URL}")
    start = time.time()
    threads = []

    for i in range(NUM_THREADS):
        t = threading.Thread(target=worker, args=(i,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f"Finished load test in {time.time() - start:.2f}s")
    print(f"Total requests sent: {NUM_THREADS * REQUESTS_PER_THREAD}")
