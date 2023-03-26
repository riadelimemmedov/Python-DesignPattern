
#!Equipment
class Equipment:
    def __init__(self,name:str,price:int):
        self.name = name
        self.price = price


#!Composite
class Composite:
    def __init__(self,name:str):
        self.name = name
        self.items = []
        
        
    def add(self,equipment:Equipment):
        self.items.append(equipment)
        return self
    
    
    @property
    def price(self):
        print('Property getter work')
        return sum([x.price for x in self.items])
    
if __name__ == '__main__':
    computer = Composite('Pc')
    cpu = Equipment('Ryzen',1000)
    display_card = Equipment('AsusGtx',2500)
    
    memory = Composite('Corsair')
    rom = Equipment('Read only memory',100)
    ram = Equipment('Random accsess memory',75)
    
    
    mem = memory.add(rom).add(ram)
    pc = computer.add(cpu).add(display_card).add(mem)
    
    print(pc.price)