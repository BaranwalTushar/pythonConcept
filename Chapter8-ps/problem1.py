def greatest_three(num1,num2,num3):
    if(num1>num2 and num1>num3):
        print(f"Greatest number is {num1}")

    elif(num2>num1 and num2>num3):
        print(f"Greatest number is {num2}")    

    elif(num3>num1 and num3>num2):
        print(f"Greatest number is {num3}") 
        return "done"

a1 = int(input("Enter the three number"))
a2 = int(input("Enter the three number"))
a3 = int(input("Enter the three number"))
print(greatest_three(a1,a2,a3))

