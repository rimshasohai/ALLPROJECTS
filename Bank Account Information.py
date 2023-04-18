class BankAccount: 
    def __init__(self,b=0): 
        self.balance=b
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
        print()
  
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount
        print('Amount to be deposited in bank:',self.balance)
    def withdraw(self):
        amount=float(input('Enter amount to be withdrawn from bank:'))
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdrew:", amount) 
        else: 
            print('\n Insufficient balance')
  
    def displaybalance(self):
        print('Net Available Balance:',self.balance) 
  
a1=BankAccount(600)
print('CHOICES')
print('1)DISPLAY BALANCE  \n2)DEPOSIT AMOUNT  \n3)WITHDRAW AMOUNT\n')

choice=int(input('ENTER THE CHOICE:'))
           
if choice==1:
           a1.displaybalance()

elif choice==2:
    a1.deposit()

elif choice==3:
    a1.withdraw()

