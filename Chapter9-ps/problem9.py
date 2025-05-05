with open("myFile1.txt") as f:
    content1 = f.read()

with open("myFile2.txt") as f:
    content2 = f.read() 
    f.r

if(content1 == content2):
    print("same")
else:
    print("Not same..")      


# For wipeout We have to use write(" ")   