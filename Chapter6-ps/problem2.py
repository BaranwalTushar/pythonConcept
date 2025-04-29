a1 = int(input("Subject 1 marks : "))
a2 = int(input("Subject 2 marks : "))
a3 = int(input("Subject 3 marks : "))
 
maximum_marks = 300
sum  = a1+a2+a3

percentage = sum/maximum_marks*100

if(a1>=33 and a2>=33 and a3>=33 and percentage>=40):
    print(f"Student is pass {percentage}%")

else:
    print(f"Student is not pass {percentage}%")
