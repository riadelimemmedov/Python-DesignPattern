
#!NetworkService
# class NetworkService:
#     def __init__(self):
#         self.components = {}
        
#     def add(self,key:str,value:str):
#         self.components[key] = value
        
#     def show(self):
#         print(self.components,end='\n')
    

# #!NetworkServiceBuilder
# class NetworkServiceBuilder:
#     def __init__(self):
#         self._service = NetworkService()
        
#     def add_target_url(self,url:str):
#         self._service.add("URL",url)
        
#     def add_auth(self,auth:str):
#         self._service.add("Authorization",auth)
        
#     def add_caching(self,cache:int):
#         self._service.add("Cache-Control",cache)

#     def build(self) -> NetworkService:
#         service = self._service
#         self._service = NetworkService()
#         return service
    
# if __name__ == "__main__":
#     builder = NetworkServiceBuilder()
    
#     builder.add_target_url('google.com')
#     service1 = builder.build()
#     service1.show()
    
    
#     builder.add_target_url('youtube.com')
#     builder.add_auth('abs123')
#     builder.add_caching(50000)
#     service2 = builder.build()
#     service2.show()



#*Method 2 but not convenient way
#--------------------------------------------------------------------------------------------------------------------------------
#!NetworkService
class NetworkService:
    def __init__(self,url:str="",auth:str="",cache:int=0):
        self.components = {}
        if url:
            self.components["URL"] = url
        if auth:
            self.components["Authorization"] = auth
        if cache:
            self.components["Cache-Control"] = cache
            
    def show(self):
        return self.components
    
    
if __name__ == '__main__':
    service1 = NetworkService(url='google.com')
    print(service1.show())
    
    service2 = NetworkService(url='youtube.com',auth='abs123',cache=50000)
    print(service2.show())