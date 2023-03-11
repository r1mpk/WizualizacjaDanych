def iloczynCiagu(*liczby):
    if len(liczby) == 0:
        print("Brak liczb!")
        return 0
    else:
        a = 1
        for i in liczby:
            a = a*i
        return a

print(iloczynCiagu(1, 5, 6, 2))
