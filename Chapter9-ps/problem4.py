with open("poem.txt") as f:
    content = f.read()

content = content.replace("Donkey","###")    

with open("poem.txt","w") as f:
    content = f.write(str(content))