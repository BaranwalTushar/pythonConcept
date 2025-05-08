class Employee :
    language = "python"
    salary = "120000"

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
     
    @staticmethod 
    def greet():
        print("Good Morning")    

harry = Employee()
harry.greet()
harry.getInfo() 