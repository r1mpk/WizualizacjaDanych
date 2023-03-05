h = eval(input("Enter diamond's height: (No less than 3, no more than 9)\n"))
if 3 <= h <= 9:
    for x in range(h):
        print(" " * (h - x), "*" * (2 * x + 1))
    for x in range(h - 2, -1, -1):
        print(" " * (h - x), "*" * (2 * x + 1))
else:
    print("Wrong height!")
