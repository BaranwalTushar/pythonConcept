with open("log.txt")  as f:
 lines  =    f.readlines() 

lineNo = 1 
for line in lines:
 if("python" in line):
  print(f"yes python is available in {lineNo}")
  
  break
 lineNo += 1
else:
 print("No Python is not present")
 
