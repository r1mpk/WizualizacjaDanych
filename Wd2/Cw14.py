from math import sqrt as sr
num = float(input("Input number\n"))
try:
    print(sr(num))
except ValueError:
    print("Your number can not be square rooted!")