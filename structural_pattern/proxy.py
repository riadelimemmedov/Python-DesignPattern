
"""
    The proxy design pattern is a structural pattern in software engineering that provides a surrogate or placeholder object to control access to another object.
    In Python, the proxy pattern can be implemented using classes.
"""

#* https://www.geeksforgeeks.org/proxy-method-python-design-patterns/ => his is great resource understant proxy design pattern for python developers



#!Subject Interface
class Payment:
    def pay(self, amount):
        pass


#!RealSubject
class BankPayment(Payment):
    def __init__(self, account_number, pin):
        self.account_number = account_number
        self.pin = pin

    def pay(self, amount):
        print(
            f"BankPayment : Pain {amount} from account {self.account_number}")


#!Proxy
class PaymentProxy(Payment):
    def __init__(self, account_number, pin):
        self.account_number = account_number
        self.pin = pin
        self.bank_payment = None

    def authenticate(self):
        if self.pin == "1234":
            return True
        else:
            return False

    def pay(self, amount):
        if self.authenticate():
            if self.bank_payment == None:
                self.bank_payment = BankPayment(self.account_number, self.pin)
            self.bank_payment.pay(amount)
        else:
            print('PaymentProxy : Incorrect PIN.Payment failed')


if __name__ == '__main__':
    payment_proxy = PaymentProxy('64278fkdhsagdja3784682', '1234')
    payment_proxy.pay(100)

    payment_proxy = PaymentProxy('64278fkdhsagdja3784682', '5124')
    payment_proxy.pay(250)
