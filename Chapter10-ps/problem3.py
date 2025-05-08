class Demo:
    a = 4 

o = Demo()
print(o.a) #prints the class attribute because instance attriute is not present 
o.a = 0    #instance attribute is set
print(o.a) #instance attribute will print
print(Demo.a) #prints the class attribute