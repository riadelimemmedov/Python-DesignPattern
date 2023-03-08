from abc import ABC,abstractmethod


#!Country
class Country:
    print('Calling Country')
    
class USA(Country):
    print('Calling Usa')
    
class Spain(Country):
    print('Calling Spain')
    
class Japan(Country):
    print('Calling Japan')    


#!CurrentFactory
class CurrentFactory(ABC):
    @abstractmethod
    def current_factory(self,country) -> str:#!Define an interface or abstract class for creating an object
        pass
    

#*FiatCurrencyFactory
class FiatCurrencyFactory(CurrentFactory):#In other words, subclasses are responsible to create the instance of the class
    def current_factory(self,country) -> str:
        if country is USA:
            return "USD"
        elif country is Spain:
            return "EUR"
        else:
            return "JPY"
        
        
#*VirifyCurrencyFactory
class VirtualCurrencyFactory(CurrentFactory):
    def current_factory(self,country) -> str:
        if country is USA:
            return "Bitcoin"
        elif country is Spain:
            return "Ethereum"
        else:
            return "Dogecoin"

#?__name__ == '__main__'
if __name__ == '__main__':#!this part for user, not creation
    f1 = FiatCurrencyFactory()
    f2 = VirtualCurrencyFactory()
    
    print(f1.current_factory(USA))
    print(f1.current_factory(Spain))
    print(f1.current_factory(Japan))
    
    print(f2.current_factory(USA))
    print(f2.current_factory(Spain))
    print(f2.current_factory(Japan))
