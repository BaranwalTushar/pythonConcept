class Employee:
    
    language = "py"
    salary = 30000


tushar = Employee()
tushar.language = "Java" #instance attribut preference is higher than the class attribute.
print(tushar.language,tushar.salary)