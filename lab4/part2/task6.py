import threading

def divide():
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Ошибка: {e}")

threads = []
for _ in range(5):
    thread = threading.Thread(target=divide)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()