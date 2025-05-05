words = ["Donkey","Ganda","Banda","Wrong"]

with open("poem.txt","r") as f:
    content = f.read()

for word in words:  
     content = content.replace(word,"#" * len(word))      

 
with open("poem.txt","w") as f:

    content = f.write(content)