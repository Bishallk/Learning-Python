
#-------ProcessPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import os
import time

def task(n):
    print(f"Process ID: {os.getpid()} is working on task {n}")
    time.sleep(2)
    return n * n


#-------using submit() method

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        # Submit tasks individually
        future1 = executor.submit(task, 1)
        future2 = executor.submit(task, 2)
        future3 = executor.submit(task, 3)
        
        # Wait for results and get them
        print(f"Result of task 1: {future1.result()}")
        print(f"Result of task 2: {future2.result()}")
        print(f"Result of task 3: {future3.result()}")


#--------using map()
if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        # Using map to run tasks in parallel
        results = executor.map(task, range(1, 4))  # Executes task on [1, 2, 3]

    # Print results
    for r in results:
        print("Result:", r)

#* The map() function blocks the program until all tasks are completed and returns the results in the order of the input.

#* Unlike submit(), which allows more fine-grained control, map() is simpler for running multiple tasks that need to return results in sequence.

#* Fine-grained control allows you to submit individual tasks to the process pool one at a time, manage them separately, and handle their results asynchronously.
