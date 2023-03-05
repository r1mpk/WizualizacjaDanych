import sys
for i in range(1, 11):
    for j in range(1, 11):
        a = str(i*j) + " "
        sys.stdout.write(a)
    sys.stdout.write("\n")