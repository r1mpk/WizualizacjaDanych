while 1 == 1:
    choice = input("Do you want to see your number squared? y/n\n")
    if choice == "y":
        a = int("Input integer\n")
        print(a*a)
    elif choice == "n":
        print("See you later!")
        break
    else:
        print("You have input wrong thing. I'll assume you're leaving.")
        break
