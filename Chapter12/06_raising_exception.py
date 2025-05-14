a = int(input("Enter a Number :"))
b = int(input("Enter second Number :"))

if(b==0):
    raise ZeroDivisionError("Hey our program does not perform division by zero")

else:
    print(f"The division is {a/b}")
