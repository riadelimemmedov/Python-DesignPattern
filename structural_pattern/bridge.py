
"""
    It works as a bridge between two incompatible interfaces. This pattern involves a single class which is responsible to join
    functionalities of independent or incompatible interfaces.
"""

from abc import ABC,abstractmethod


#!Device
class Device(ABC):
    volume = 0
    
    
    @abstractmethod
    def get_name(self)->str:
        pass
    

#!Radio
class Radio(Device):
    def get_name(self) -> str:
        return f"Radio {self}"
    

#!TV
class Tv(Device):
    def get_name(self) -> str:
        return f"Tv {self}"

###################################################################    

#!Remote
class Remote(ABC):
    @abstractmethod
    def volume_up(self):
        pass
    
    @abstractmethod
    def volume_down(self):
        pass
    
    
#!BasicRemote
class BasicRemote(Remote):
    def __init__(self,device:Device):
        self.device = device
        
    def volume_up(self):
        self.device.volume+=1
        print(f"{self.device.get_name()} volume up : {self.device.volume}")
        
    def volume_down(self):
        self.device.volume -= 1
        print(f"{self.device.get_name()} volume down : {self.device.volume}")
    
        
if __name__ == '__main__':
    
    radio = Radio()
    tv = Tv()
    
    radio_remote = BasicRemote(radio)
    tv_remote = BasicRemote(tv)
    
    radio_remote.volume_up()
    radio_remote.volume_up()
    radio_remote.volume_down()
    
    tv_remote.volume_up()
    tv_remote.volume_down()
    tv_remote.volume_up()
    tv_remote.volume_up()