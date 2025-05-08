class Calculator:
    def __init__(self,n):
        self.n =n

    def square(self):
        print(f"the square is{self.n*self.n}")
        
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")    

    def squareRoot(self):
        print(f"The squareroot is {int(self.n**1/2)}")    

    @staticmethod
    def greet():
        print("Hello...")    


a = Calculator(2)
a.squareRoot() 
a.greet()
        