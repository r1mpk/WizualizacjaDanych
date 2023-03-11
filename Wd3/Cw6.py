import math

def przeciwprostokatna(a, b):
    c = math.sqrt(a*a + b*b)
    print(c)

a = input("Pierwsza przyprostokatna\n")
b = input("Druga przyprostokatna\n")

przeciwprostokatna(int(a), int(b))