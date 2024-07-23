import multiprocessing
import time

def cpu_intensive_task(n):
    count = 0
    for i in range(n):
        count += i
    print(f"Completed task with count {count}")

n = 10**7
processes = []
start_time = time.time()

for _ in range(4):
    process = multiprocessing.Process(target=cpu_intensive_task, args=(n,))
    processes.append(process)
    process.start()

for process in processes:
    process.join()

end_time = time.time()
print(f"Process CPU-bound task took {end_time - start_time} seconds")
