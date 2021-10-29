menu = int(input("   ORDER PLEASE \n 1.pasta \n 2. pizza \n 3. sandwitch \n \n Select Yours"))
if menu == 1 :
    print("\n pasta $10 ")

    confirm = int(input("\n confirm to press one"))
    if confirm ==1:
        print("\n Order confirmed")
    else:
        print("chose correct option")
elif menu == 2:
    print("\n with hotsause $15")
    confm = int(input("\nconfirm to press.one"))

    if confm == 1:
        print("\n Order confirmed")
    else:
        print("chose correct option")
elif menu == 3:
    print("\n with extra cheese $20")
    confirm = int(input("\n confirm to press one"))
    if confirm == 1:
        print("\n Order confirmed")
    else:
        print("chose correct option")
else:
    print("\n WRONG SELECTION")