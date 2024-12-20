from collections import Counter
Item = {"Water": 300, "Milk": 200, "Coffee": 100}
print("We have these varieties of coffees:")

def sub():
    global Item
    result=dict(Counter(Item)-Counter(Item1))
    Item=result

i=1
while i>=1:
    print("1:espresso\n2:lattle\n3:cappuccino")
    cof = int(input("Please enter the coffee number you want:"))
    if cof == 1:
        water=50
        milk=70
        coffee=18
        price=25
        Item1= {"Water": 50, "Milk": 70, "Coffee": 18}
        sub()
    elif cof == 2:
        water=200
        milk=150
        coffee=24
        price=25
        Item1 = {"Water": 200, "Milk": 150, "Coffee": 24}
        sub()
    elif cof == 3:
        water=250
        milk=100
        coffee=24
        price=35
        Item1 = {"Water": 250, "Milk": 100, "Coffee": 24}
        sub()
    else:
        print("Please enter the valid item")
    if Item.values() not in Item1.values():
        print("The Price is Rs.", price)
        Amt = int(input("Please pay the amount here:"))
        if Amt > price:
            ext = Amt-price
            print("Rs.",ext," is returned")
            print("Thank you")
        elif Amt < price:
            less = Amt-price
            print("Please pay the balance amount of Rs.:",-(less))
            amt = int(input())
            print("Thank You")
        else:
            print("Your payment is successfull\nThank you for using our machine")
    else:
        print("There are insufficient ingridents")

                # For Adding another Coffee
    i=int(input("Do you want to take another coffee(1:Yes/0:No)"))
print("Remainig Items=",Item)