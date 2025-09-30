import numpy as np 

keys , latitude , longitude ,postalCode = np.genfromtxt("FastFoodRestaurants.csv" , delimiter=',' , usecols = ( 3 , 4 , 5 , 7 ) , unpack= True , dtype = None , skip_header= 1 , invalid_raise= False)

print(latitude)
print(longitude)
print(postalCode)

print("\nStatistics formulas : ")
print("\nmean of key  : " , np.mean(keys))
print("Average of key : " , np.average(keys))
print("std of keys : " , np.average(keys))
print("median of postalcode : " , np.median(postalCode))
print("percentile - 15 of price : " , np.percentile(longitude , 15))
print("percentile - 25 of price : " , np.percentile(latitude , 25))
print("percentile - 3 of price : " , np.percentile(postalCode , 3))

print("\nMath formulas : ")
print("\nbed square : " , np.square(keys))
print("\nbed squareroot : " , np.sqrt(keys))
print("\nbath power : " , np.power(keys , 2))
print("\nbath abs : " , np.abs(keys))

print("\nArithmatic formulas : ")
addition = latitude + longitude
print("Addition : " , addition )
subtraction = latitude - longitude
print("subtracttion : " , subtraction) 
multiplication = latitude * longitude
print("multipliction : " , multiplication)
division = latitude / longitude
print("division : " , division)

print("\nTrignomatric formulas : ")
sine_value = np.sin(keys)
print("sin : " , sine_value)
cosine_value = np.cos(longitude)
print("cos : " , cosine_value)
tangent_value = np.tan(latitude)
print("tan : " , tangent_value)
sineh_value = np.sinh(keys)
print("sin : " , sineh_value)
cosineh_value = np.cosh(latitude)
print("cos : " , cosineh_value)
tangenth_value = np.tanh(latitude)
print("tan : " , tangenth_value)


print("\nLogrithum formulas : ")
print("natural logrithum value : " , np.log(postalCode))
print("base10 logrithum value : " , np.log10(postalCode))

print("\nArrays : ")
D22 = np.array([latitude , longitude])
print("D2 Array : " , D22)
print("Dimention : " , D22.ndim)
print("Size : " , D22.size)
print("Shape : " , D22.shape)
print("Dtype : " , D22.dtype )

print("\nScilcing : ")
print("Splicing array - D2[:1,:5] : " , D22[:1 , :5])
print("Splicing array - D2[:1,4:15:5] : " , D22[:1 , 4:15:5])

print("\nIndexing : ")
print("Indexing [0,1] : " , D22[0,1])
print("Indexing [0,6] : " , D22[0,6])

print("\nIndexing one my one : ")
for elem in np.nditer(D22):
    print(elem)

print("\nIndexing row by row with index : ")
for index, elem in np.ndenumerate(D22):
    print(index, elem)

print("Rehspae : " , np.reshape(D22 , (2 , 200)))
print("Dimention : " , D22.ndim)
print("Size : " , D22.size)
print("Shape : " , D22.shape)
print("Dtype : " , D22.dtype )

