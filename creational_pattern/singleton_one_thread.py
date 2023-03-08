
#Note:
    #This code example if we have create singleton instance one thread its normally create one instance
    #But if we have create create same instance multi thread same time what do you do? => Using Thread Library
#--------------------------------------------------------------------------------------------------------------------------------

#!Singleton
class Singleton(type):
    _instances = {}
    
    def __call__(self,*args,**kwargs):#call class and create new instances from class
        if self not in self._instances:
            print('Self does not exits')
            instance = super().__call__(*args,**kwargs)
            self._instances[self] = instance
        print('Self exits exits')
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
if __name__ == '__main__':
    s1 = create_singleton()
    s2 = create_singleton()
