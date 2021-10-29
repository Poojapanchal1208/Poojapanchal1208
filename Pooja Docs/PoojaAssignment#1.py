import sys



def Menu():
    print("...........Menu.........")
    print("1:Grilled Sandwich $10 ")
    print("2:Hakka Noodles $22 ")
    Snacks = int(input("Choose your snack:"))
    if Snacks == 1:
        price = 10
        return price, str("Grilled Sandwich")
    else:
        price = 22
        return price, str("Hakka Noodles")


def Afterorder():
    global totalprice,invoice
    price, selectedsnacks = Menu()
    quantity = input("Total amount of today's snack :")
    print(".....Your snacks.....")
    print("Order \t      Item Amt \t   Item Price \t   Total")

    price = int(price)
    quantity = int(quantity)
    totalprice = price * quantity
    totalprice = str("{:.2f}".format(totalprice))

    invoice=str(selectedsnacks) + "\t  " + str(quantity) + "\t  $" + str("{:.2f}".format(price)) + "\t $" + totalprice
    print(invoice)


def custinfo():
    print("Warm Welcome to Amazing Eats")
    firstname = input("Enter Firstname:")
    lastname = input("Enter Lastname:")

    print("........Home Adress.......")
    streetno = input("Enter Street No:")
    streetname = input("Enter Street Name:")
    city = input("Enter City:")
    province = input("Enter province:")
    postalcode = input("Enter postal code:")
    instruction = input("Enter instruction:")
    phonenumber = input("Enter phone number:")

def Confirmsnack():
    conf=input("Would you like to confirm your snack: \n Press Y|y or y \n Press N|n \n Select your choice: ")
    return conf

def Student():
    conf = input("Are you Student? \n Press Y|y to confirm \n Press N|n to deny \n Select your choice:")
    return conf

def showStudentinvoice(amount,GSTAmount,totalprice):
    print("Order \t      snack Amount \t   snack Price \t   Total")
    print(invoice)


    print("10% Savings \t \t \t \t  -$"+str("{:.2f}".format(amount)))
    print("\t \t \t \t  Total \t \t $"+str("{:.2f}".format(totalprice-amount)))
    print("\t \t \t \t  Tax (13 %) \t $"+str("{:.2f}".format(GSTAmount)))
    
    print("\t \t \t \t \t \t    FinalAmount \t $"+str("{:.2f}".format(GSTAmount+totalprice-amount)))
    #print("\t \t \t Total -$"+GSTAmount)

def showCustinvoice(GSTAmount,totalprice):
    print("Order \t      Snack amount \t   Snack amount \t   Total")
    print(invoice)


    print("\t \t \t \t \t  Total \t \t $"+str("{:.2f}".format(totalprice)))
    print("\t \t \t \t \t  Tax (13 %) \t $"+str("{:.2f}".format(GSTAmount)))
    
    print("\t \t \t \t \t  TOTAL \t $"+str("{:.2f}".format(GSTAmount+totalprice)))

custinfo()
Menu()
c = Confirmsnack()

if c=="Y" or c=="y":
        ans=Student()
        if ans=="Y" or ans=="y":
            tempamt = float(totalprice)
            studentAmt=(tempamt * 10)/100
            GSTAmount=((tempamt - studentAmt) * 13)/100
            showStudentinvoice(float(studentAmt),float(GSTAmount),float(totalprice))
        elif ans=="N" or ans=="n":
            tempamt = float(totalprice)
            GSTAmount=((tempamt) * 13)/100
            showCustinvoice(float(GSTAmount),float(totalprice))


elif Confirmsnack()=="N" or Confirmsnack()=="n":
    Menu()