class Employee:
    company = "itc"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


# class Programmer:

#     company  = "ITC infotech"    
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")    

#     def showLangauge(self):
#          print(f"The name is {self.name} and the language is {self.language}")    

class Programmer(Employee):
    company = "ITC Limited"
    def showLanguage(self):
        print(f"the name is {self.name} and he is good with {self.language}")



a = Employee()
b = Programmer()

print(a.company, b.company)