class Vector:

    def __init__(self,x,y,z):

        self.x = x
        self.y = y
        self.z = z

    def __add__(self,other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result

    def __mul__(self,other):
          result = self.x * other.x + self.y * other.y + self.z * other.z
          return result   
    
    def __str__(self):
         return f"{self.x}i  {self.y}j , {self.z}k"
        

v = Vector(1,2,3)
w = Vector(3,4,5)     

print(v+w)
print(v*w)