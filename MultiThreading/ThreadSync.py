
#-------Synchronization

import threading
import time
start_time=time.time()
balance=200
lock=threading.Lock()

def deposit(amount,times,lock):
    global balance
    for _ in range(times):
        lock.acquire()
        balance+=amount
        lock.release()


def withdraw(amount,times,lock):
    global balance
    for _ in range(times):
        lock.acquire()
        balance-=amount
        lock.release()


#creating thread

deposit_thread=threading.Thread(target=deposit,args=(5,1000,lock))
withdraw_thread=threading.Thread(target=withdraw,args=(5,1000,lock))

deposit_thread.start()
withdraw_thread.start()
deposit_thread.join()
withdraw_thread.join()
print(balance)

end_time=time.time()
print(f"time taken :{end_time-start_time}")

    
