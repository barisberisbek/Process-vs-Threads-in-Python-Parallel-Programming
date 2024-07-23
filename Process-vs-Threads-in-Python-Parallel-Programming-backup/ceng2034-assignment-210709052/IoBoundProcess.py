import multiprocessing
import requests
import time

def download_file(url):
    response = requests.get(url)
    print(f"Downloaded {url} with size {len(response.content)} bytes")

urls = [
    'https://file-examples.com/storage/fe15076da466528199d9c5a/2017/10/file_example_JPG_500kB.jpg',
    'https://file-examples.com/storage/fe15076da466528199d9c5a/2017/10/file_example_JPG_1MB.jpg',
    'https://file-examples.com/storage/fe15076da466528199d9c5a/2017/10/file_example_JPG_2500kB.jpg'
]

processes = []
start_time = time.time()

for url in urls:
    process = multiprocessing.Process(target=download_file, args=(url,))
    processes.append(process)
    process.start()

for process in processes:
    process.join()

end_time = time.time()
print(f"Process I/O-bound task took {end_time - start_time} seconds")
