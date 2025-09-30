# dictionary 

a = {
    "firstname" : "momina" ,
    "LASTname" : "idrees" , 
    "age" : 21 ,
    "okayy" : True 
}

print(type(a))

print(a.keys())
print(a.values())

a.update({"color" : "white"})
a.pop("age")

print(a)