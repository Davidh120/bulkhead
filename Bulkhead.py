import concurrent.futures
import time

# Thread pools for different services
service_a_pool = concurrent.futures.ThreadPoolExecutor(max_workers=10)
service_b_pool = concurrent.futures.ThreadPoolExecutor(max_workers=10)

count = 0

def handle_service_a():
    global count
    count += 1
    # Simulate work by sleeping
    time.sleep(1)
    # Simulate a failure
    if count > 5:
        raise Exception("Fallo por numero de intentos")

def handle_service_b():
    # Simulate work by sleeping
    time.sleep(1)

# Function to submit tasks to the thread pools
def submit_tasks():
    service_a_future = service_a_pool.submit(handle_service_a)
    service_b_future = service_b_pool.submit(handle_service_b)
    try:
        service_a_future.result()
        print("Doing Service A")
    except Exception as e:
        print(f"Service A failed: {e}")

    try:
        service_b_future.result()
        print("Doing Service B")
    except Exception as e:
        print(f"Service B failed: {e}")

# Submit tasks in a loop to simulate continuous operation
while True:
    submit_tasks()
    time.sleep(2)  # Wait a bit before submitting new tasks
