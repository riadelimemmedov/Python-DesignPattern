from abc import ABC,abstractmethod


#!FoodType
class FoodType:
    french = 1
    american = 2


#!Restaurant
class Restaurant(ABC):
    print('Restaurant class call')
    @abstractmethod
    def make_food(self):
        pass
    
    @abstractmethod
    def make_drink(self):
        pass
    
    
#!FrenchRestaurant
class FrenchRestaurant(Restaurant):
    print('French Restuaratnt')
    def make_food(self):
        print('Cordon Blue')
        
    def make_drink(self):
        print('Merlo')
        
        

#!AmericanRestaurant
class AmericanRestaurant(Restaurant):
    print('American Restuaratnt')
    def make_food(self):
        print('Hamburger')
        
    def make_drink(self):
        print('Coca cola')
        
        

#!RestoreaurantFactory
class RestoreaurantFactory:
    print('RestaurantFactory class call')
    @staticmethod   
    def suggest_restaurant(r_type:FoodType):
        if r_type == FoodType.french:
            return FrenchRestaurant()
        else:
            return AmericanRestaurant()
        
        
#*dine_at
def dine_at(restaurant:Restaurant):
    print('For dinner we are having')
    restaurant.make_food()
    restaurant.make_drink()
    

# __name__ == '__main__'
if __name__ == '__main__':
    suggestion1 = RestoreaurantFactory.suggest_restaurant(FoodType.french)
    suggestion2 = RestoreaurantFactory.suggest_restaurant(FoodType.american)
    
    dine_at(suggestion1)
    dine_at(suggestion2)

