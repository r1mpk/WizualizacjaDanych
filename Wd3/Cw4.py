def monotone(a):
    if a > 0:
        print("Rosnaca")
    elif a == 0:
        print("Stala")
    elif a < 0:
        print("Malejaca")

a = input("Input a for y = ax + b.\n")
b = input("Input b for y = ax + b.\n")
monotone(int(a))