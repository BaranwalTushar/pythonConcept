class Employee :
  
    def __init__(self,name,salary,language): #dunder method which is automatically called.
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object...")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
     
    @staticmethod 
    def greet():
        print("Good Morning")    

harry = Employee("Tushar",127181,"Kotlin")
print(harry.name,harry.salary,harry.language)