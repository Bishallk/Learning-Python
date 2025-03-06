
#-----------------M U L T I T H R E A D I N G-----------------|

#------Process
#* Process is an instance of computer program that is being executed .

#------Thread
#* Thread is an entity within a process that can be scheduled for execution.
#* Thread is a sequence  of such instructiona within a program that can be executed independently of other code. 
#* Thread is a subset of process.

#------Multithreading
#* Multithreading is defined as the ability of a processer to execute multiple threads concurrently.

#* Example

from time import sleep, time
import threading


start_time=time()
def even(end):
    for i in range(2,end,2):
        print(i)
        

def odd(end):
     for i in range(1,end,2):
        print(i)


       

t1= threading.Thread(target=odd, args=[100])
t2= threading.Thread(target=even, args=[100])

t1.start()
t2.start()

t1.join()
t2.join()
end_time=time()
print(f"total time taken by {__name__}: {end_time-start_time}")




    
    