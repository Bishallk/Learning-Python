
class CountObj:
    __counter=0
    @property
    def get_counter(self):
        return self.__counter
    @staticmethod
    def total_objects():
        print()
            
    def __init__(self):
        print("Object Created..")
        CountObj.get_couter+=1

obj=CountObj()
obj=CountObj()
obj=CountObj()
obj=CountObj()
obj=CountObj()
print()