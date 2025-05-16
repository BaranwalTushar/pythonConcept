from functools import reduce

l = [23,25,40,56,50,32]

def maxNum(a,b):
  
   if(a>b):
      return a
   return b


print(reduce(maxNum,l))