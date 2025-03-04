import threading,time,requests,subprocess

# the real us of threading is to run multiple tasks at the same time.
# here in the example i'll open a calcualtor app and then print the statetment but
# the statement will be printed before the calculator app is opened.

# def open_app(app_name):
#     time.sleep(5)
#     subprocess.Popen(app_name)
    
# t1=threading.Thread(target=open_app,args=("calc",))
# t1.start()
# print("App is opened")


# def task():
#     """Print numbers from 1 to 5."""
#     for i in range(1, 6):
#         print(f"Task running: {i}")
#         time.sleep(0.001)

# t1=threading.Thread(target=task)
# t1.start()
# # t1.join()
# print("Done ")


# Why us threadings?



URLS = [
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/2"
]

def fetch_url(url):
    response = requests.get(url)
    print(f"Fetched {url} in {response.elapsed.total_seconds()} seconds")

start_time = time.time()

# threads = []
# for url in URLS:
#     thread = threading.Thread(target=fetch_url, args=(url,))
#     thread.start()  # Starts executing the function in a new thread
#     threads.append(thread)  # Store thread reference

# # Wait for all threads to complete
# for thread in threads:
#     thread.join()

# end_time = time.time()
# print(f"Total time taken (with threading): {end_time - start_time:.2f} seconds")
#   output exepceted
# Fetched https://httpbin.org/delay/2 in 3.166547 seconds
# Fetched https://httpbin.org/delay/2 in 3.180288 seconds
# Fetched https://httpbin.org/delay/2 in 3.908508 seconds
# Total time taken (with threading): 3.92 seconds

# BUT WIHTOUT THREADING


URLS = [
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/2"
]

def fetch_url(url):
    response = requests.get(url)
    print(f"Fetched {url} in {response.elapsed.total_seconds()} seconds")

start_time = time.time()


# for url in URLS:
#     fetch_url(url=url) 


end_time = time.time()
print(f"Total time taken (without threading): {end_time - start_time:.2f} seconds")


# witout threading the output will be
# Fetched https://httpbin.org/delay/2 in 3.602332 seconds
# Fetched https://httpbin.org/delay/2 in 3.13651 seconds
# Fetched https://httpbin.org/delay/2 in 3.305915 seconds
# Total time taken (without threading): 10.06 seconds



# WHY USE JOIN?
# If you don't use join, the main thread will not wait for the child thread to complete.
# The main thread will continue its execution and will not wait for the child thread to complete.
# output without and with join()
# with join 

# Task running: 1
# Task running: 2
# Task running: 3
# Task running: 4
# Task running: 5
# Done

# without join
# Task running: 1Done 

# Task running: 2     
# Task running: 3     
# Task running: 4     
# Task running: 5    

# so basically join connects the threads and waits for the child thread to complete before the main thread completes.

# def task1():
#     """Print numbers from 1 to 5 for Task 1."""
#     for i in range(1, 6):
#         print(f"Task1 running: {i}")
#         time.sleep(0.001)

# def task2():
#     """Print numbers from 1 to 5 for Task 2."""
#     for i in range(1, 6):
#         print(f"Task2 running: {i}")
#         time.sleep(0.001)
        


# t1=threading.Thread(target=task1)
# t2=threading.Thread(target=task2)

# t1.start()
# t2.start()  

# t1.join()
# t2.join()

# print("Task1 and Task2 are completed!")

# Using a Lock to Protect a Shared Resource


counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock:  # Ensures only one thread updates 'counter' at a time
        counter += 1

# threads = [threading.Thread(target=increment) for _ in range(1000)]
# for thread in threads:
#     thread.start()
# for thread in threads:
#     thread.join()

# print(f"Final counter value with lock: {counter}")  # Always 1000


# Why Use the Lock Here?
# Without the lock, multiple threads could read, modify, and write the counter concurrently (a race condition). This might lead to lost updates, and the final value could be less than the expected value. The lock prevents these overlapping operations.

# The main thread creates 1000 thread objects and starts them one after another. Each thread is scheduled by the operating system to run concurrently. However, because the increment operation is guarded by a lock, only one thread can execute it at any moment.


# What Happens Without the Lock
# Consider the following steps executed concurrently by two threads:

# Thread A reads counter (say it’s 10).
# Thread B reads counter (also 10).
# Thread A increments its local copy to 11.
# Thread B increments its local copy to 11.
# Thread A writes 11 back to counter.
# Thread B writes 11 back to counter.

# The final value of counter is 11, but it should be 12. This is a lost update. The lock prevents this situation by ensuring that only one thread can modify the counter at a time.


# Daemon Threads
# Daemon threads run in the background and are terminated when the main program exits. They are useful for background tasks that should not block the application from closing.

def background_task():
    while True:
        print("Running in background...")
        time.sleep(1)

# daemon_thread = threading.Thread(target=background_task, daemon=True)
# daemon_thread.start()

# # Main program waits a few seconds before exiting
# time.sleep(5)
# print("Main program exits, daemon thread will be killed.")


