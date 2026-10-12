import threading
import time

def brew_coffe():
    print(f"{threading.current_thread().name} started brewing...")
    count = 0

    # do some time consuming computation
    for _ in range(100_000_000):
        count += 1
    
    print(f"{threading.current_thread().name} finished brewing...")

def brew_instant_coffe():
    print(f"{threading.current_thread().name} started brewing...")
    count = 0

    # do some time consuming computation
    # the no of iterations here is less compared to function `brew_coffe`
    for _ in range(100_000_00):
        count += 1
    
    print(f"{threading.current_thread().name} finished brewing...")

thread_1 = threading.Thread(target=brew_instant_coffe, name="Barista-1")
thread_2 = threading.Thread(target=brew_coffe, name="Barista-2")

start_time = time.time()
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
end_time = time.time()

print(f"Total Time Take: {end_time - start_time:.2f} seconds")
