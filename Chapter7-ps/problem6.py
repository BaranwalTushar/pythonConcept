# n = int(input("Enter the number : "))
# fact = 1

# while(n>0):
#     fact *= n
#     n -= 1 
# print(fact)    

n = int(input("Enter the number : "))
fact = 1
for i in range(1,n+1):
    fact = fact*i
print(f"Factorial of {n} is : {fact}")    