import sys



def Menu():
    print("----------------Menu---------------")
    print("1:sandwich  $10")
    print("2:pasta  $2")
    meal = int(input("Select Meal:"))
    if meal == 1:
        price = 10
        return price, str("sandwich")
    else:
        price = 2
        return price, str("pasta")


def aMenu():
    global totalbill,invoice
    price, Meal = Menu()
    quantity = input("How many meals are order today:")
    print("---------------------Your Order--------------------")
    print("Order \t      Item Amt \t   Item Price \t   Total")

    price = int(price)
    quantity = int(quantity)
    totalbill = price * quantity
    totalbill = str("{:.2f}".format(totalbill))

    invoice=str(Meal) + "\t  " + str(quantity) + "\t\t   $" + str("{:.2f}".format(price)) + "\t\t $" + totalbill
    print(invoice)


def custId():
    print("Warm Welcome to  Amazing eats")
    firstname = input("Enter Firstname:")
    lastname = input("Enter Lastname:")

    print("----------------------Home address---------------------")
    streetno = input("Enter Street No:")
    streetname = input("Enter Street Name:")
    city = input("Enter City:")
    province = input("Enter province:")
    postalcode = input("Enter postal code:")
    instruction = input("Enter instruction:")
    phonenumber = input("Enter phone number:")

def finalsnack():
    conf=input("Would you like to confirm your order: \n Press Y|y or y \n Press N|n \n Select your choice: ")
    return conf

def cStudent():
    conf = input("Are you Student: \n Press Y|y to confirm \n Press N|n to deny \n Select your choice:")
    return conf

def Studentinvoice(amt,GSTAmount,totalbill):
    print("Order \t      Item amount \t   Item Price \t   Total")
    print(invoice)


    print("10% Savings \t \t \t \t \t -$"+str("{:.2f}".format(amt)))
    print("\t \t \t \t   Total \t \t $"+str("{:.2f}".format(totalbill-amt)))
    print("\t \t \t \t Tax (13 %) \t $"+str("{:.2f}".format(GSTAmount)))
    
    print("\t \t \t \t \t \t \t   Final amount \t $"+str("{:.2f}".format(GSTAmount+totalbill-amt)))
    

def Custinvoice(GSTAmount,totalbill):
    print("Order \t      Item amount \t   Item Price \t   Total")
    print(invoice)


    print("\t \t \t \t \t  Total \t \t $"+str("{:.2f}".format(totalbill)))
    print("\t \t \t \t \t  Tax (13 %) \t $"+str("{:.2f}".format(GSTAmount)))
                
    print("\t \t \t \t \t    Final amount \t $"+str("{:.2f}".format(GSTAmount+totalbill)))

custId()
aMenu()
co = finalsnack()

if co=="Y" or co=="y":
        ans=cStudent()
        if ans=="Y" or ans=="y":
            temamount = float(totalbill)
            studentAmount=(temamount * 10)/100
            GSTAmount=((temamount - studentAmount) * 13)/100
            Studentinvoice(float(studentAmount),float(GSTAmount),float(totalbill))
        elif ans=="N" or ans=="n":
            temamount = float(totalbill)
            GSTAmount=((temamount) * 13)/100
            Custinvoice(float(GSTAmount),float(totalbill))


elif finalsnack()=="N" or finalsnack()=="n":
    aMenu()