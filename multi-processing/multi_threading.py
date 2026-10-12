import threading
import time

def take_order():
    for i in range(1, 4):
        print(f"Taking Order for customer {i}")
        time.sleep(2)

def brew_coffe():
    for i in range(1, 4):
        print(f"Brewing Coffe for customer {i}")
        time.sleep(4)

# A thread takes an executor function as an argument
order_thread = threading.Thread(target=take_order)
brew_thread = threading.Thread(target=brew_coffe)

order_thread.start()
brew_thread.start()

# wait for both the thread to finish and join back to the main thread
order_thread.join()
brew_thread.join()

print("All orders served successfully!!")