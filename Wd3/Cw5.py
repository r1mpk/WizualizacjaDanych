def lineRelativity(a, b):
    if a == b:
        print("Rownolegla")
    elif a*b == -1:
        print("Prostopadla")
    else:
        print("Ani rownolegla, ani prostopadla")

a = input("Input a1\n")
b = input("Input a2\n")
lineRelativity(int(a), int(b))