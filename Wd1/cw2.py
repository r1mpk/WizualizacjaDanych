def dodawanie(a, b):
    print( a + b)
def odejmowanie(a, b):

    
    print( a - b)
def dzielenie (a, b):
    print(a / b)
def mnozenie (a, b):
    return a * b

a = input("Input your variable A")
b = input("Input your variable B")
dzialanie = input("Choose your operation")
if(dzialanie == dodawanie):
    print(dodawanie(a, b))
elif(dzialanie == odejmowanie):
    print(odejmowanie(a, b))
elif(dzialanie == dzielenie):
    print(dzielenie(a, b))
elif(dzialanie == mnozenie):
    print(mnozenie(a, b))
