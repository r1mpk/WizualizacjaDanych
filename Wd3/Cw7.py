def sumaCiagu(a, r, n):
    return int(((2*a+(n-1)*r)/2)*n)

a = int(input("Podaj pierwszy wyraz ciagu\n"))
r = int(input("Podaj roznice ciagu\n"))
n = int(input("Podaj ile wyrazow zsumowac\n"))
print(sumaCiagu(a, r, n))