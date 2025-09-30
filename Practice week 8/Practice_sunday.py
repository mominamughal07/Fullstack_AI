#list
print("         >>  lIST   <<")
book_list = [0000 , "ALCHEMICS" , 2015 , 200.5 , True ]
print("book list : " , book_list)
print(f"Whole list type : " , type(book_list))
print(f"type of 3rd item : " , type(book_list[2]))

for item in book_list:
    print(item)

book_list.append("MOMINA")
book_list.insert(1 , "idrees")
print("After append and insert : " , book_list )

book_list.remove(200.5)
book_list.pop(2)
print("list after remove and pop : " , book_list)


print("------------------------------------------")
print("\n")