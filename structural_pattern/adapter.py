
#! It works as a bridge between two incompatible interfaces. This pattern involves a single class which is responsible to join
#!functionalities of independent or incompatible interfaces.


class PowerSocket():
    """
        PowerSocket base class
    """
    
    def __init__(self,holeNum,holShape,holVolt):
        self.num_holes = holeNum
        self.shape_holes = holShape
        self.volt_holes = holVolt
        
        
    def getHoleNum(self):
        return self.num_holes
    
    def getHoleShape(self):
        return self.shape_holes
    
    def getHoleVolt(self):
        return self.volt_holes
    

#define custom type of power socket for each country
class chineseSocket(PowerSocket):
    def __init__(self):
        super().__init__(3,"FLAT",220)

class europeanSocket(PowerSocket):
    def __init__(self):
        super().__init__(2,"ROUND",250)
        
class taiwaneSocket(PowerSocket):
    def __init__(self):
        super().__init__(2,"FLAT",110)
        
class martianSocket(PowerSocket):
    def __init__(self):
        super().__init__(2,"FLAT",300)



#My plug 
class chinise3pinPlug():#think for computer socket plug format this code
    def __init__(self):
        self.pins = 3
        self.volt = 220
        self.pinshape = "FLAT"


class RedmiLaptop():
    def __init__(self):
        self.plug = chinise3pinPlug()
        self.__adapter = None
        
    def addAdapter(self,adpt):
        self.__adapter = adpt
    
    def charge(self,inSocket,powerInWatt):
        res = False
        if (isinstance(inSocket,PowerSocket)):
            if self.__adapter.convert(inSocket):
                socket = self.__adapter.getSocket()
                print('work always not does not matter true or false res value')
                res=(self.plug.pins == socket.getHoleNum()) and \
                    (self.plug.pinshape == socket.getHoleShape()) and \
                    (self.plug.volt == socket.getHoleVolt())
        else:
            print("Socket is not instance of PowerSocket")
        
        if res:
            current = round(powerInWatt / self.plug.volt,2)
            print("Start charging... Power: {} watt; Socket current : {} am ... ".format(str(powerInWatt),str(current)))
            
        else:
            print('Socket and plug not compatible, impossible to charge')
        return res
    
    
class SocketAdapter():
    """
        SocketAdapter base class
    """
    
    def __init__(self):
        pass
    
    def convert(self):
        pass
    
    
    def getSocket(self):
        pass


class AnyToChineseAdapter(SocketAdapter):
    """
        A concrete SocketAdapter class that can convert any socket to chinese socket
    """
    
    def __init__(self):
        super().__init__()
        self.__outSocket = chineseSocket()
        self.__voltRatio = 1
        self.__plug = ""
        
        
    def convertSocket(self,fromSocket):
        res = True
        if isinstance(fromSocket,chineseSocket):
            self.__voltRatio = 1
            self.__plug = "Chinese format plug"
            print("Chinese to Chinese using {}".format(self.__plug))
        elif isinstance(fromSocket,europeanSocket):
            self.__voltRatio = 1
            self.__plug = "European format Plug"
            print("European to Chinese using {}".format(self.__plug))
        elif isinstance(fromSocket,taiwaneSocket):
            self.__voltRatio = 2
            self.__plug = "Taiwanese format plug"
            print("Taiwanese to Chinese using {}".format(self.__plug))
        else:
            print("Unknown socket cannot choose plug format and volt convertion ratio")
            res = False
        
    def getSocket(self):
        return self.__outSocket

    def getVoltRatio(self):
        return self.__voltRatio

    
if __name__ == '__main__':
    laptop = RedmiLaptop() #create instance from RedmiLaptop class
    
    #I am in china mainland
    chSocket = chineseSocket()
    laptop.charge(socket=chSocket,powerInWatt=235)
    
    euSocket = europeanSocket()
    laptop.charge(socket=euSocket,powerInWatt=235)
    
    twSocket = taiwaneSocket()
    laptop.charge(socket=twSocket,powerInWatt=235)
