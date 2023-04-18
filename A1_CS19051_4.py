#OBJECT:FOOD
#VARIABLES:
samosas_price=10
rolls_price=15
chocolates_price=10
chips_price=10
tea_price=10
biscuits_price=10
samosas_in_stock=0
rolls_in_stock=0
biscuits_in_stock=0
chips_in_stock=0
tea_in_stock=0
chocolates_in_stock=0
bonus=0
total_sales=0
total_items=samosas_in_stock+rolls_in_stock+biscuits_in_stock+chips_in_stock+tea_in_stock+chocolates_in_stock

      
#FUNCTIONS
#1.SHOWING OF ITEMS THAT ARE IN STOCK
def stock():
   global total_items
   t=total_items
   print()
   print('THE TOTAL ITEMS ARE:',t)
   print()


#2TAKE ORDER,PRINT BILL,ADJUST STOCK
def order():
      global samosas_in_stock,rolls_in_stock,biscuits_in_stock,chips_in_stock,tea_in_stock,chocolates_in_stock
      samosas_in_stock=samosas_in_stock+int(input('ENTER TOTAL NO OF SAMOSAS IN STOCK:'))
      rolls_in_stock=rolls_in_stock+int(input('ENTER TOTAL NO OF ROLLS IN STOCK:'))
      biscuits_in_stock=biscuits_in_stock+int(input('ENTER TOTAL PACKETS OF BISCUITS IN STOCK:'))
      chips_in_stock=chips_in_stock+int(input('ENTER TOTAL PACKETS OF CHIPS IN STOCK:'))
      tea_in_stock=tea_in_stock+int(input('ENTER CUPS OF TEA IN STOCK:'))
      chocolates_in_stock=chocolates_in_stock+int(input('ENTER BARS OF CHOCOLATES IN STOCK:'))
      print('HEY! WELCOME TO OUR TEATIME SHOP.WHAT DO YOU WANT? THIS IS OUR MENU.PLEASE ORDER.')
      print('ITEMS              PRICE\n1.SAMOSAS               10\n2.ROLLS                     15\n3:CHOCOLATE           10\n4:CHIPS                     10\n5:TEA                        10\n6:BISCUITS               10')
      order_samosas=int(input('HOW MANY SAMOSAS DO YOU WANT?'))
      order_rolls=int(input('HOW MANY ROLLS DO YOU WANT?'))
      order_chocolates=int(input('HOW MANY CHOCOLATES DO YOU WANT?'))
      order_biscuits=int(input('HOW MANY BISCUITS DO YOU WANT?'))
      order_chips=int(input('HOW MANY PACKECTS OF CHIPS DO YOU WANT?'))
      order_tea=int(input('HOW MANY CUPS OF TEA DO YOU WANT?'))
      
      if order_samosas>=samosas_in_stock:
         order_samosas=samosas_in_stock
         samosas_in_stock=0
         print('SAMOSA THAT ARE IN STOCK:',samosas_in_stock)

      if order_rolls>=rolls_in_stock:
         order_rolls=rolls_in_stock
         rolls_in_stock=0
         print('ROLLS THAT ARE IN STOCK:',rolls_in_stock)

      if order_biscuits>=biscuits_in_stock:
         order_biscuits=biscuits_in_stock
         biscuits_in_stock=0
         print('BISCUITS THAT ARE IN STOCK:',biscuits_in_stock)

      if order_chips>=chips_in_stock:
         order_chips=chips_in_stock
         chips_in_stock=0
         print('CHIPS THAT ARE IN STOCK:',chips_in_stock)

      if order_chocolates>=chocolates_in_stock:
         order_chocolates=chocolates_in_stock
         chocolates_in_stock=0
         print('CHOCOLATES THAT ARE IN STOCK:',chocolates_in_stock)

      if order_tea>=tea_in_stock:
         order_tea=tea_in_stock
         tea_in_stock=0
         print('TEA THAT ARE IN STOCK:',tea_in_stock)

      if order_samosas<samosas_in_stock:
         samosas_in_stock-=order_samosas
         print('SAMOSAS THAT ARE IN STOCK:',samosas_in_stock)
         global total_items
         total_items+=samosas_in_stock
         
      if order_rolls<rolls_in_stock:
         rolls_in_stock-=order_rolls
         print('ROLLS THAT ARE IN STOCK:',rolls_in_stock)
         total_items+=rolls_in_stock
         
      if order_chocolates<chocolates_in_stock:
         chocolates_in_stock-=order_chocolates
         print('CHOCOLATES THAT ARE IN STOCK:',chocolates_in_stock)
         total_items+=chocolates_in_stock
         
      if order_biscuits<biscuits_in_stock:
         biscuits_in_stock-=order_biscuits
         print('BISCUITS THAT ARE IN STOCK:',biscuits_in_stock)
         total_items+=biscuits_in_stock
         
      if order_chips<chips_in_stock:
         chips_in_stock-=order_chips
         print('CHIPS THAT ARE IN STOCK:',chips_in_stock)
         total_items+=chips_in_stock
         
      if order_tea<tea_in_stock:
         tea_in_stock-=order_tea
         print('TEA THAT ARE IN STOCK:',tea_in_stock)
         total_items+=tea_in_stock
      
      a=order_samosas*samosas_price
      b=order_rolls*rolls_price
      c=order_chocolates*chocolates_price
      d=order_biscuits*biscuits_price
      e=order_chips*chips_price
      f=order_tea*tea_price
    
      bill=a+b+c+d+e+f
      print('                TOTAL BILL        ')
      print('SAMOSA:',                       f'{(a)}')
      print('ROLLS:',                           f'{(b)}')
      print('CHOCOLATES:',             f'{(c)}')
      print('BISCUITS:',                      f'{(d)}')
      print('CHIPS:',                            f'{e}')
      print('TEA:',                                f'{f}')
      print()
      print('TOTAL BILL:',                 f'{bill}')
      print()
      total_items=0
      total_items=samosas_in_stock+rolls_in_stock+biscuits_in_stock+chips_in_stock+tea_in_stock+chocolates_in_stock
      global total_sales
      total_sales+=bill
   



#3.ADDING ITEMS TO THE STOCK
def new_items():
   global samosas_in_stock
   samosas_new=int(input('ENTER NEW AMOUNT OF SAMOSAS:'))
   samosas_in_stock+=samosas_new
   global  rolls_in_stock
   roll_new=int(input('ENTER NEW AMOUNT OF ROLLS:'))
   rolls_in_stock+=roll_new
   global  biscuits_in_stock
   biscuits_new=int(input('ENTER NEW PACKETS OF BISCUITS:'))
   biscuits_in_stock=biscuits_in_stock+biscuits_new
   global chips_in_stock
   chips_new=int(input('ENTER NEW PACKETS OF CHIPS:'))
   chips_in_stock=chips_in_stock+chips_new
   global tea_in_stock
   tea_new=int(input('ENTER NEW CUPS OF TEA:'))
   tea_in_stock=tea_in_stock+tea_new
   global  chocolates_in_stock
   chocolates_new=int(input('ENTER NEW PACKETS OF CHOCOLATE:'))
   chocolates_in_stock=chocolates_in_stock+chocolates_new
   global total_items
   total_items=samosas_in_stock+rolls_in_stock+biscuits_in_stock+chips_in_stock+tea_in_stock+chocolates_in_stock

#OBJECT:EMPLOYEES
#VARIABLES:
wage_rate=25000
day=30
count=0


#FUNCTIONS:

#1.ENTER EMPLOYEES INFO:
def employee_info():
   name=input('ENTER THE NAME OF EMPLOYE:')
   designation=input('ENTER THE DESIGNATION OF AN EMPLOYEE:')
   age=int(input('ENTER THE AGE OF AN EMPLOYEE:'))
   print()



#2.ENTER EMPLOYEES HOURS FOR A MONTH
def employee_hours():
    global count
    for i in range(1,day+1):
       print('ENTER NO OF HOURS A EMPLOYEE WORKED IN A DAY OUT OF 10 HOURS:',end=' ')
       no_of_hours=int(input())
       count+=no_of_hours
    print('THE NO OF HOURS A EMPLOYE WORKED IN A MONTH:',count)
    print()
    

#3.EMPLOYEES BONUS/
def employee_bonus():
    global total_sales
    if total_sales>1000:
       global bonus
       bonus+=12000
    print('THE BONUS IS',bonus)
    print()

    
#4.CALCULATION OF EMPLOYEES PAYMENT
def employees_payment():
   global bonus
   global wage_rate
   global count
   
   if count<=100:
      u=wage_rate+5000+bonus
      print('THE PAYMENT OF AN EMPLOYEE WILL BE:',u)
      print()
      count=0
      bonus=0
   elif count>100 and count<=199:
      j=wage_rate+10000+bonus
      print('THE PAYMENT OF AN EMPLOYEE WILL BE:',j)
      print()
      count=0
      bonus=0
   elif count>=200:
      k=wage_rate+20000+bonus
      print('THE PAYMENT OF AN EMPLOYEE WILL BE:',k)
      print()
      count=0
      bonus=0
   elif count>=300:
      m=wage_rate+30000+bonus
      print('THE PAYMENT OF AN EXCELLENT EMPLOYEE WILL BE:',m)
      print()
      count=0
      bonus=0
