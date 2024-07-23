import threading
import time

def cpu_intensive_task(n):
    count = 0
    for i in range(n):
        count += i
    print(f"Completed task with count {count}")

n = 10**7
threads = []
start_time = time.time()

for _ in range(4):
    thread = threading.Thread(target=cpu_intensive_task, args=(n,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
print(f"Threaded CPU-bound task took {end_time - start_time} seconds")
