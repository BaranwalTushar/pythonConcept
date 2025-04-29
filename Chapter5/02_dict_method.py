d = {} #empty dictionary

marks = {
    "Key" : "Value",
    "Harry" : 100,
    "Tushar" : 98,
    "vaibhav" : 0,
}

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Harry":99})
print(marks)

print(marks.get("Harry2"))#prints none
print(marks["Harry2"]) # return error
