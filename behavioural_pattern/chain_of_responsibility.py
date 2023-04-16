class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if self.successor is not None:
            print('Wtf')
            return self.successor.handle_request(request)
        else:
            print('Wtf2')
            return None

class ConcreteHandler1(Handler):
    def handle_request(self, request):
        if request == 'request1':
            print('tapildi axirki request1')
            return "Handled by ConcreteHandler1"
        else:
            return super().handle_request(request)

class ConcreteHandler2(Handler):
    def handle_request(self, request):
        if request == 'request2':
            return "Handled by ConcreteHandler2"
        else:
            print('Bam request 1 tapilmadi request2 de')
            return super().handle_request(request)

class ConcreteHandler3(Handler):
    def handle_request(self, request):
        if request == 'request3':
            return "Handled by ConcreteHandler3"
        else:
            print('Bam request 1 tapilmadi request3 de')
            return super().handle_request(request)

if __name__ == '__main__':
    handler1 = ConcreteHandler1()#returun None Handler
    handler2 = ConcreteHandler2(handler1)
    handler3 = ConcreteHandler3(handler2)
    print(handler3.handle_request('request1'))
    # print(handler3.handle_request('request2'))
    # print(handler3.handle_request('request3'))
    #print(handler3.handle_request('unknown request'))
