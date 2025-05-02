def natural_num(num):
    if(num==1 ):
        return 1
    sum =0
    sum = num+natural_num(num-1)
    return sum

a = int(input("Enter a num : "))
print(f"the sum of {a} natural no. is : {natural_num(a)}")