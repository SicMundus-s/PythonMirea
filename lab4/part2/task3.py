import queue
import threading

my_queue = queue.Queue()

def producer():
    for i in range(1, 6):
        my_queue.put(i)

def consumer():
    while True:
        item = my_queue.get()
        if item is None:
            break
        print(item)
        my_queue.task_done()

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
my_queue.join()

my_queue.put(None)
consumer_thread.join()