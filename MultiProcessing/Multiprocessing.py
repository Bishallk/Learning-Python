
#---------- M U L T I P R O C E S S I N G--------|

#* Multiprocessing allows a program to run multiple processes in parallel, utilizing multiple CPU cores.
#* This is useful for CPU-bound Tasks

#* Example
from multiprocessing import Process

def task(name):
    print(f"Process {name} is running")

if __name__ == "__main__":
    p1 = Process(target=task, args=("A",))
    p2 = Process(target=task, args=("B",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

