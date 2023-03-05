lista = []
while 1 == 1:
    choice = input("Do you want to add new number to your list? y/n\n")
    if choice == "y":
        num = int(input("Input your number\n"))
        lista.append(num)
    elif choice == "n":
        print("Your full list is: ", lista)
        print("When its sorted, it is ", sorted(lista))
        break
    else:
        print("Wrong input. Your list is ", lista)
        print("When its sorted, it is ", sorted(lista))
        break
