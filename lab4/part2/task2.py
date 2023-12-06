import threading

mutex = threading.Lock()

def print_numbers():
    with mutex:
        for i in range(1, 6):
            print(i)

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers)

thread1.start()
thread2.start()

thread1.join()
thread2.join()