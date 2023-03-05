num = input("Input your multidigit number\n")
i = 0
a = 0
while i < len(num):
    a += int(num[i])
    i += 1
print("Sum of the digits of your number is", a)
