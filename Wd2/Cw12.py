import sys
for i in range(1, 10):
    for j in range(1, 10):
        a = str(i*j) + " "
        sys.stdout.write(a)
    sys.stdout.write("\n")