from typing import Counter


print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
>
"""
)
menu=['wings', 'cookies', 'spring rolls', 'salmon', 'steak', 'meat tornado','a literal garden', 'ice Cream', 'cake', 'pie', 'coffee', 'tea', 'unicorn tears']

# fill counter using for loop to make it easy when adding item on menu
count=[]
for i in range (len(menu)):
    count.append(0)
    

# user input
# x=input('>').lower()
# print(x)

the_order=input('>')
# check if order on menu
while the_order!="quit":
    if the_order.lower() in menu:
        # target index of order 
        index_of_item=menu.index(the_order.lower()) 
        count[index_of_item]+=1
        print(f"** {count[index_of_item]} order of {the_order} have been added to your meal **")
    else:
        print("please choose from menu")
    the_order=input('>')
print("Thank You for your visit")

