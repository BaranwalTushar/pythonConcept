# n = int(input("Enter the number : "))
# for i in range(1,11):
#    print(f"{n}*{11-i} = {n*(11-i)}")



#second method using list to print reverse table
list =[]
n = int(input("Enter a number"))
for i in range(1,11):
    list.append(f"{n}*{i} = {n*i}")

for reverse in reversed(list):
    print(reverse)