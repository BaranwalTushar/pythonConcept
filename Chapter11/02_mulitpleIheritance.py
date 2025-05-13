class Employee:
    name = "Tushar"
    salary= 10190
    company = "itc"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the language here is your language {self.language}")

class Programmer(Employee,Coder):
    company = "ITC Limited"
    def showLanguage(self):
        print(f"the name is {self.company} and he is good with {self.language}")



a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()