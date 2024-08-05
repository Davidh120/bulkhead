import time

count = 0

def handle_service_a():
    global count
    count += 1
    # Simulate work by sleeping
    time.sleep(1)
    # Simulate a failure
    if count > 5:
        raise Exception("Fallo por numero de intentos")

    print("Doing A")
    
def handle_service_b():
    # Simulate work by sleeping
    time.sleep(1)

    print("Doing B")

# Function to submit tasks to the thread pools
def submit_tasks():
    handle_service_a()
    handle_service_b()

# Submit tasks in a loop to simulate continuous operation
while True:
    submit_tasks()
    time.sleep(2)  # Wait a bit before submitting new tasks
