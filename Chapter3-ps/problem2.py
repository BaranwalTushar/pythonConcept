letter = ''' Dear <|Name|>, 

             You are selected!
             
             <|Date|>'''

print(letter.replace("<|Name|>","Tushar").replace("<|Date|>","06-09-2001"))