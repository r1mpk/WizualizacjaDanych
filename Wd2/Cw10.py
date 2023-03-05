height = int(input("Input the height of the pyramid. \n"))
if height <= 10:
    i = 1
    a = ""
    while i <= height:
        a = a + "A"
        print(a)
        i += 1
else:
    print("Error: wrong height!")
