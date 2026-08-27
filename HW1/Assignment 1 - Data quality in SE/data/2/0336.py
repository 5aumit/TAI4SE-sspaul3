class User:
    account = []
    def __init__(self,balance,int_rate):
        self.balance = balance
        self.int_rate = int_rate
        User.account.append(self)
    def dep(self,amount):
        self.balance += amount
        return self

    def make_withdrawal(self,amount):
        if(self.balance-amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds:Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(self.balance)  #print(f"Balance:{self.balance}")
        return(self)
    
    def yield_interest(self):
        # self.balance+=(self.balance*self.int_rate)#times by a decimal gets you a smaller number
        self.balance=self.balance+self.balance*self.int_rate
        return(self)

    @classmethod
    def we_call_cls(cls):
        for account in cls.account:
            account.display_account_info()
    

class Jedi:
    def __init__(self,name):
        self.name = name #this means that its name is its name.
        self.account = {
            "Grey": User(5000,.3),
            "light": User(300,.33)
            }

prey=Jedi('prey')
print(prey.name)


prey.we_call_cls()



