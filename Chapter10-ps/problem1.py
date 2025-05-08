class programmer:
    
    company = "microsoft"
    
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = programmer("Harry",12000,221010)
print(p.name,p.company,p.salary,p.pin)        