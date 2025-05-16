from functools import reduce
#Map function

l = [1,2,3,4,5]
square = lambda x: x*x

sqList = map(square,l)
print(list(sqList))


#filtter

def even(n):
    if(n%2==0):
        return 1
    return 0

onlyEven = filter(even,l)
print(list(onlyEven))


#Reduce

def sum(a,b):
    return a+b


print(reduce(sum,l))