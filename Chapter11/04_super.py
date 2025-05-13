class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of Prorammer")
    b=2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
        
    c=3


# o =  Employee()
# print(o.a)    

# p = Programmer()
# print(p.a,p.b)

q = Manager()
print(q.a,q.b,q.c)