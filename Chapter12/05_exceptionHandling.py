try:
    a = int(input("Enter a Number :"))
    print(a)

except ValueError as v:

    print("Hi...")
    print(v)

except Exception as e:
    print(e)

print("Thankyou")        