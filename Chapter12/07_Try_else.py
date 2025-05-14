try:
    a = int(input("Enter a number :")) # when try will successfully run then it will go in else block. otherwise no
    print(a)

except Exception as e:
    print(e)    

else:
    print("I am inside else")    

finally:
    print("I am in finally")    