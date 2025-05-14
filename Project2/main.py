import random

n = random.randint(1,100)
a = -1
guess = 0
while(a != n):
    guess += 1

    a = int(input("Enter a number :"))
    if(a>n):
        print("Please enter lower number")

    elif(a<n):
        print("please enter Higher number")

print(f" The number is {n} and You  guessed correct number in {guess} attempt")        