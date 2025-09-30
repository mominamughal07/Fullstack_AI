book_list = {0000 , "ALCHEMICS" , 2015 , 200.5 , True }

print("Type : " , type(book_list))
book_list.add("BOOK DETAILS")
print("After add :" , book_list )

book_list.discard(200.5)
print(book_list)