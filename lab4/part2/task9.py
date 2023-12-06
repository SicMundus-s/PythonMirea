import queue
import threading

task_queue = queue.Queue()

def task_handler():
    while True:
        task = task_queue.get()
        if task is None:
            break
        print(f"Выполнение задачи: {task}")
        task_queue.task_done()

def add_tasks():
    for i in range(1, 11):
        task_queue.put(f"Задача {i}")

worker_threads = []
for _ in range(5):
    worker = threading.Thread(target=task_handler)
    worker_threads.append(worker)
    worker.start()

add_tasks()

task_queue.join()

for _ in range(5):
    task_queue.put(None)

for worker in worker_threads:
    worker.join()