import random

computer = random.choice([-1,0,1])
youstr = input("Enter your Choice : ")
youDict = {"s" : 1, "w" : -1, "g" :0}

reverseDict = {1:"snake", -1:"water", 0:"gun"}

you = youDict[youstr]

print(f"you choose {reverseDict[you]}\n computer choose {reverseDict[computer]}")

if(computer == you):
    print("Match Draw...")

else:
    if(computer == -1 and you == 1):
        print("You win!")   
    elif(computer == -1 and you == 0):
        print("You lose!")    
    elif(computer == 1 and you == -1):
        print("you loss!")   
    elif(computer == 1 and you == 0):
        print("You win!")    
    elif(computer == 0 and you == 1):
        print("You win!")   
    elif(computer == 0 and you == -1):
        print("You lose!")  
    else:
        print("Something went wrong")      