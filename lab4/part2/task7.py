import threading

total = 0
lock = threading.Lock()

def increase_total():
    global total
    for _ in range(1000000):
        with lock:
            total += 1

thread1 = threading.Thread(target=increase_total)
thread2 = threading.Thread(target=increase_total)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Общее значение: {total}")