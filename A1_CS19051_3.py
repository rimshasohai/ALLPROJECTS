#OBJECT:BOUTIQUE
#VARIABLES
dress_in_stock=0
maxi_in_stock=0
tshirts_in_stock=0
jeans_in_stock=0
total_item_s=dress_in_stock+maxi_in_stock+tshirts_in_stock+jeans_in_stock
dress_price=3000
maxi_price=5000
tshirt_price=500
jeans_price=1500

#FUNCTIONS

#1.SHOWING ITEMS
def boutique_stock():
    global  total_item_s
    to=total_item_s
    print()
    print('THE TOTAL ITEMS THAT ARE IN STOCK:',total_item_s)
    print()


#2.TAKE ORDER,TAKE BILL AND ADJUST STOCK
def order_customer():
    global dress_in_stock,maxi_in_stock,tshirts_in_stock,jeans_in_stock
    dress_in_stock=dress_in_stock+int(input('ENTER DRESSES THAT ARE IN STOCK:'))
    maxi_in_stock=maxi_in_stock+int(input('ENTER NUMBER OF MAXI THAT ARE IN STOCK:'))
    tshirts_in_stock=tshirts_in_stock+int(input('ENTER NUMBER OF T-SHIRTS THAT ARE IN STOCK:'))
    jeans_in_stock=jeans_in_stock+int(input('ENTER NUMBER OF JEANS THAT ARE IN STOCK:'))
    print()
    print('HEY!WELCOME TO OUR BOUTIQUE.HOW CAN I HELP YOU')
    print()
    order_dress=int(input('HOW MANY DRESSES DO YOU WANT?'))
    order_tshirts=int(input('HOW MANY T-SHIRTS DO YOU WANT?'))
    order_maxi=int(input('HOW MANY MAXI DO YOU WANT?'))
    order_jeans=int(input('HOW MANY PAIR OF JEANS DO YOU WANT?'))

    if order_dress>=dress_in_stock:
        order_dress=dress_in_stock
        dress_in_stock=0
        print('THE DRESSES THAT ARE IN STOCK:',dress_in_stock)
        
    if order_maxi>=maxi_in_stock:
        order_maxi=maxi_in_stock
        maxi_in_stock=0
        print('THE MAXI THAT ARE IN STOCK:',maxi_in_stock)

    if  order_tshirts>=tshirts_in_stock:
        order_tshirts=tshirts_in_stock
        tshirts_in_stock=0
        print('THE T-SHIRTS THAT ARE IN STOCK:',tshirts_in_stock)
    
    if order_jeans>=jeans_in_stock:
        order_jeans=jeans_in_stock
        jeans_in_stock=0
        print('THE JEANS THAT ARE IN STOCK:', jeans_in_stock)
        
    lo=order_jeans*jeans_price
    qo=order_tshirts*tshirt_price
    mo=order_maxi*maxi_price
    too=order_dress*dress_price
    
    if  order_dress<dress_in_stock:
        global total_item_s
        dress_in_stock-=order_dress
        print('DRESS THAT IS IN STOCK:',dress_in_stock)
        total_item_s+=dress_in_stock
    if  order_tshirts<tshirts_in_stock:
        tshirts_in_stock-=order_tshirts
        print('TSHIRTS THAT ARE IN STOCK:',tshirts_in_stock)
        total_item_s+=tshirts_in_stock
    if  order_maxi<maxi_in_stock:
        maxi_in_stock-=order_maxi
        print('MAXI THAT ARE IN STOCK:',maxi_in_stock)
        total_item_s+=maxi_in_stock
    if  order_jeans<jeans_in_stock:
        jeans_in_stock-=order_jeans
        print('JEANS THAT ARE IN STOCK:',jeans_in_stock)
        total_item_s+=jeans_in_stock
    total_bill=lo+mo+too+qo
    print('TOTAL BILL')
    print()
    print('DRESS:',                  f'{(too)}' )
    print('MAXI:',                      f'{(mo)}')
    print('JEANS:',                   f'{(lo)}')
    print('T-SHIRTS:',              f'{(qo)}')
    print()
    print('TOTAL BILL:',          f'{(total_bill)}')
    total_item_s=0
    total_item_s=total_item_s=dress_in_stock+maxi_in_stock+tshirts_in_stock+jeans_in_stock

        
#3.ADDITION OF ITEMS IN STOCK
def add_items():
    global dress_in_stock
    dress_new=int(input('ENTER NEW DRESSES THAT COME IN STOCK:'))
    dress_in_stock+=dress_new
    global  tshirts_in_stock
    tshirts_new=int(input('ENTER NEW TSHIRTS THAT COME IN STOCK:'))
    tshirts_in_stock+=tshirts_new
    global  jeans_in_stock
    jeans_new=int(input('ENTER PAIR OF JEANS THAT COME IN STOCK:'))
    jeans_in_stock+=jeans_new
    global  maxi_in_stock
    maxi_new=int(input('ENTER MAXI THAT COME IN STOCK:'))
    maxi_in_stock+=maxi_new
    global total_item_s
    total_item_s=dress_in_stock+tshirts_in_stock+jeans_in_stock+maxi_in_stock
