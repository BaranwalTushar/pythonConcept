l = [23,25,40,56,50,32]

def divideByFive(n):
   
        if(n%5==0):
            return True
        return False

ans = filter(divideByFive,l)
print(list(ans))