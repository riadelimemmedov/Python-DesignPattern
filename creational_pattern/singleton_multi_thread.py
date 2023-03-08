import time
from threading import Thread,Lock 


#Note:
    #We want to create single instance class multi thread environmen,I mean we create one class instance different object thread at pc
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#!Singleton
class Singleton(type):
    _instances = {}
    _lock = Lock()
    
    def __call__(self,*args,**kwargs):#for creating new instance
        with self._lock:#The with statement in Python is used for resource management and exception handling. You’d most likely find it when working with file streams.# For example, the statement ensures that the file stream process doesn’t block other processes if an exception is raised, but terminates properly    
            if self not in self._instances:
                instance = super().__call__(*args,**kwargs)
                time.sleep(1)
                self._instances[self] = instance
        return self._instances[self]
    

#!NetworkDriver
class NetworkDriver(metaclass=Singleton):
    def log(self):
        print(f"{self}\n", self)
        

#*create_singleton
def create_singleton():
    singleton = NetworkDriver()
    singleton.log()
    return singleton

#?__name__ == __main__ 
if __name__ == "__main__":
    #Multi Thread
    p1 = Thread(target=create_singleton)
    p2 = Thread(target=create_singleton)
    p1.start()
    p2.start()