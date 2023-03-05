import sys

print("Input integer value")
s = sys.stdin.readline()
print("Input another integer value  ")
d = sys.stdin.readline()
e = int(s)*int(d)
sys.stdout.write("Their multiplication is ")
sys.stdout.write(str(e))
