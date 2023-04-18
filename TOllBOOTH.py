class Tollbooth:
    def __init__(self,c=0,e=0,m=0):
        self.cars1=c
        self.cars2=e
        self.money=m
    def choice(self):
        k=input('ENTER THE CHOICE IF USER PRESS P FOR CALCULATING PAYING CAR AND N FOR CALCULATING NO PAY CAR:')
        if k=='P':
            self.payingCar()
        elif k=='N':
            self.nopayCar()
    def payingCar(self):
        self.cars1+=1
        self.money+=50
    def nopayCar(self):
        self.cars2+=1
    def display(self):
        n=input('ENTER ESC TO DISPLAY THE TOTAL OR ELSE COME OUT OF PROGRAM BY CLICKING ANYTHING:')
        if n=='ESC':
            print('THE TOTAL PAYING CARS ARE:',self.cars1)
            print('THE TOTAL NON PAYING CARS ARE:',self.cars2)
            print('THE TOTAL CARS ARE:',self.cars1+self.cars2)
            print('THE TOTAL MONEY IS:',self.money)
        else:
            pass
e=Tollbooth(4,3)
e.choice()
e.display()
