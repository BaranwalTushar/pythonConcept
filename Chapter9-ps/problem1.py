with open("poem.txt")  as f:
    content = f.read()
    print(content)

if("twinkle" in content):
    print("twinkle is present")

else:
    print("Not present")