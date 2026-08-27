'''class Computer:
    def _init_(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

        
    def config(self,cpu,ram):
        print("config is", cpu, ram)




com1=Computer()
com2=Computer()


com1.config("i5",8)
com2.config("i3",16)'''
#*******************************
class Bankaccount:
    print("welcome sir/madam:")
    amount=0
    def __init__(self,name):
        
        self.name=name
        
        
    def deposit(self):
        amount=int(input("enter amount:"))
        self.amount+=amount
        print("amount deposited:",amount)
    def withdraw(self):
        amount=int(input("enter amount:"))
        if self.amount>=amount:
            self.amount-=amount
            
            print("amount withdrawn:",amount)
        else:
            print("insufficient funds")
            
    def balance(self):
        print("net balance is:",self.amount)


b = Bankaccount("subbu")
print(b.name)
b.deposit()
b.withdraw()
b.balance()
print("Thankyou sir/madam,Have a nice day:")
#********************************************************
#class vendingmachine:
   
        
            
    
      












                
            
            
        






























