#tuple

book_list = (0000 , "ALCHEMICS" , 2015 , 200.5 , True)
print("Tuple : " , book_list)
print("tuple type : " , type(book_list) )

print("Tuple second last value : " , book_list[-2])

for i in book_list:
    print(i)

print("Error :" ,book_list.append(2))



