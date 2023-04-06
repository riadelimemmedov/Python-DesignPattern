
"""
    The word Facae means the face of a building or particualarly an outer lying interface of a complex system,consist of several sub-systems
    It is an essential part Gang of Four design pattern
    It provides an easier way to access methods of the underlying systems by providing a single entry point
"""

#* https://www.geeksforgeeks.org/facade-method-python-design-patterns/ => his is great resource understant decorator design pattern for python developers


from dataclasses import dataclass

#!ComplexCachingSystem
class ComplexCachingSystem:
    def __init__(self,filepath:str):
        self.filepath = filepath
        self.cache = {}
        print(f"Reading data from file : {filepath}")
        
        
    def store(self,key:str,value:str):
        self.cache[key] = value
        print(f"Store data to cache successfully to file {self.filepath}")
        
    def read(self,key:str):
        print('Read data from cache successfully')
        return self.cache[key]
    
    def commit(self):
        print('Storing cached send to : {self.filepath}')
        

#?User data class
@dataclass
class User:#In python, a data class is a class that designed to only hold data values.They aren't different from regular classes,but usually don't have any other methods
    login:str
    


#!UserRepository
class UserRepository:
    def __init__(self):
        self.system_preferences = ComplexCachingSystem("/data/cache/user")
        
    
    def save(self,user:User):
        self.system_preferences.store("sBX29WLsGZjr1j340n2bmsLwnoOXN03B",user.login)
        
    
    def find_user(self):
        return User(self.system_preferences.read("sBX29WLsGZjr1j340n2bmsLwnoOXN03B"))
    

if __name__ == '__main__':
    user_repo = UserRepository()
    user = User('John')
    
    user_repo.save(user)
    
    retrieved_user = user_repo.find_user()
    print('Retrieved User Is ', retrieved_user.login)
    