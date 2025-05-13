class Employee:
    salary = 200
    increment = 20
     
    @property  # with this i can with .opertaor like e.salaryAfterIncrement
    def salaryAfterIncerement(self):
        return self.salary + (self.salary*self.increment)/100
    

    @salaryAfterIncerement.setter
    #new salary = old salary (1+increment/100) with this formula i get increment
    def salaryAfterIncrement(self,salary):#this salary shows after increment wala
        self.increment = ((salary/self.salary)-1)*100
        print(salary)
        print(self.salary)
    
    
e = Employee()

print(f"Salary after increment {e.salaryAfterIncerement}")
e.salaryAfterIncrement = 234
print(e.increment)
