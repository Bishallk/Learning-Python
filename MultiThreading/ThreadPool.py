
#-------Thread Pool Executors------|

#* -> Thread pool allows to manage multiple threads efficiently by reusing them insted of creating new ones repeatedly.

#* -> Useful when you need to run multiple tasks concurrently but want to limit the number of active threads to avoid excessive resource consumption.

#* How Threadpool Works Internally:
#- 1.Thread Pool Creation

#* -> When a ThreadPoolExecutor is initialized, a fixed number of threads  (max_workers) are created in advance.

#- 2.Task Submission
#* -> When a new task is submitted using submit() or map(), it is placed in a task queue.

#- 3.Thread Reuse
#* -> Idle threads in the pool pick up tasks from the queue and execute them.
#* -> Once a thread completes a task, it does not exit but waits for the next task.

#- 4.Efficient Resource Utilization
#* -> If all threads are busy, new tasks wait in the queue.
#* -> If a thread is free, it picks the next available task instead of creating a new thread.

#* Example 

from time import time,sleep
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

s_time=time()

def something(id,sleeptime):
    print(f"going to sleep:{id}-> {threading.current_thread().name}")
    sleep(sleeptime)
    return f"{id}->woken Up"

#------- ThreadPool
with ThreadPoolExecutor() as exe:
    t=exe.submit(something,1,0.5) #sumbit
    print(t.result())


#--------using as_completed method // if multiple tasks
with ThreadPoolExecutor() as executor:
    tasks=[executor.submit(something,i,0.1) for i in range(10)]
    for _ in as_completed(tasks):
        print(_.result())

#---------using map method
ids=[11,12, 13, 14, 15]
sleep_times=[0.2,0.4,0.5,0.1,0.7]
with ThreadPoolExecutor() as e:
    results=e.map(something,ids,sleep_times) 
    #returns list of outputs of given method
    for result in results:
        print(result)

#--------setting max workers
with ThreadPoolExecutor(max_workers=3) as executor:
    tasks=[executor.submit(something,i,2) for i in range(10)]
    for task in as_completed(tasks):
        print(task.result())


#* Example
def task():
    print(f"Running in: {threading.current_thread().name}")
    sleep(2)

with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(task)
    executor.submit(task)

sleep(1)  # Give some time for the thread to start
print("Active Threads:", threading.enumerate())

e_time=time()
print(f"Main thread Ended in {e_time-s_time} secs")

