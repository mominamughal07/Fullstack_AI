import numpy as np

indexing , compnay , valuation , country , city = np.genfromtxt("Startups in 2021 end.csv",delimiter=',',usecols=(0 , 1 , 2 , 4 ,5),unpack=True,dtype=str, skip_header=1,invalid_raise=False)

print(indexing)
print(compnay)
print(valuation)
print(country)
print(city)

valuation = np.char.replace(valuation, "$", "")

valuation = valuation.astype(float)
indexing = indexing.astype(float)

print("\n        Statistics          ")
print("Arithmetic mean of valuation : " , np.mean(valuation))
print("Average of indexing : " , np.average(indexing))
print("median of valuation : " , np.median(valuation))
print("percentile - 15 of valuation : " , np.percentile(valuation , 15))
print("percentile - 25 of valuation : " , np.percentile(valuation , 25))
print("percentile - 75 of valuation : " , np.percentile(valuation , 75))
print("minimum of valuation : " , np.min(valuation))
print("maximum of valuation : " , np.max(valuation))

print("\n        Mathematic          ")
print("square of valuation : " , np.square(valuation))
print("squareroot of valuation : " , np.sqrt(valuation))
print("power of valuation : " , np.power(valuation , 2))
print("absolute value of valuation : " , np.abs(valuation))

print("\n        Trignometric Functions          ")
print("Sin of indexing : " , np.sin(indexing))
print("Cos of indexing : " , np.cos(indexing))
print("Tan of indexing : " , np.tan(indexing))
print("Contant : " , np.pi)

print("\n        Exponential & logrithmic          ")
print("Exponential of indexing : " , np.exp(indexing))
print("LOG of indexing : " , np.log(indexing))
print("LOG 10 of indexing : " , np.log10(indexing))


print("\n        Hyperbolic Funcion         ")
print("sinh of valuation : " , np.sinh(valuation))
print("cosh of valuation : " , np.cosh(valuation))
print("tanh of valuation : " , np.tanh(valuation))

print("\n        Inverse Hyperbolic Functions         ")
print("inverse sin of valuation : " , np.arcsinh(valuation))
print("inverse cos of valuation : " , np.arccosh(valuation))

print("\n         Array Properties        ")
new_array = np.array([valuation , indexing])
print("creating 2d array : " ,  new_array)
print("dimension of new_array  " , new_array.ndim )
print("total no of elemnts of new_array  " , new_array.size )
print("size of array dimention of new_array  " , new_array.shape )
print("data type of new_array  " , new_array.dtype )
print("reshaping of new_array  " , new_array.reshape(6, 312) )


print("\n         Array Sllicing        ")
#Only the first row (:1)
#The first five columns (:5)
print(" Only the first row (:1) & The first five columns (:5) : " ,  new_array[:1,:5])
print(" Only the second row & The first five columns : " ,  new_array[1:2, 0:5])
print(" Rows 0 to 5 (six rows) & Columns 3 to 9 (seven columns " ,  new_array[0:6 , 3:10])

print("\n         printing all the value in the array      ")
for x in np.nditer(new_array):
    print(x)

print("\n         printing all the value including index in the array      ")
for index, x in np.ndenumerate(new_array):
    print("{} index {} value".format(index , x))




