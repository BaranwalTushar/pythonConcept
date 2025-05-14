try:
    a = int(input("Enter first number :"))
    b = int(input("Enter second number :"))
    result = a/b
    print(result)

except ZeroDivisionError as e:
  print("infinite")
