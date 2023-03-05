a = int(input("Input first number\n"))
b = int(input("Input second number\n"))
c = int(input("Input third number\n"))
if a > 0 and a <= 10:
    if a > b or b > c:
        print("First number belongs to the (0; 10> range and either \n"
              "first number is greater than second or second is greater than third.")
    else:
        print("First number belongs to the (0; 10> range, but it isn't \n"
          "greater than second nor second is greater than third.")
else:
    print("First number doesnt belong to the (0; 10> range.")
