# class Number:
#     def __init__(self,n):
#         self.n = n

#     def __add__(self,num):
#         return self.n + num.n 
    
#     def __str__(self):
#         return str(self.n)
    

# n = Number(1)
# m = Number(2)
# o = Number(3)

# result = n+m+o

# print(result)



class Number:
    def __init__(self,n):
        self.n = n

    def __add__(self,num):
        return Number(self.n + num.n) 
    
    def __str__(self):
        return str(self.n)
    

n = Number(1)
m = Number(2)
o = Number(3)

result = n+m+o

print(result)
