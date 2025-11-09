import requests
import threading
import time

URL = "http://51.20.96.40:5000/apidocs/"

NUM_THREADS = 20
REQUESTS_PER_THREAD = 50

def send_requests():
    for _ in range(REQUESTS_PER_THREAD):
        try:
            response = requests.get(URL)
            print(response.status_code)
        except Exception as e:
            print("Error:", e)
        time.sleep(0.1)

threads = []
for _ in range(NUM_THREADS):
    t = threading.Thread(target=send_requests)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
