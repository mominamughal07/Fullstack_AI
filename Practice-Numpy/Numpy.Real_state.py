import numpy as np 

broker1_id  , status , price , bed , bath , city , state = np.genfromtxt("RealEstate-USA.csv" , delimiter=',' , usecols = (0 , 1 , 2 , 3 , 4 , 7 , 8) , unpack= True , dtype = None , skip_header= 1 , invalid_raise= False)

print(broker1_id)
print(status)


print("\nStatistics formulas : ")
print("\nmean of price  : " , np.mean(price))
print("Average of beds : " , np.average(bed))
print("std of bath : " , np.average(bed))
print("median of bed : " , np.median(bed))
print("percentile - 15 of price : " , np.percentile(price , 15))
print("percentile - 25 of price : " , np.percentile(price , 25))
print("percentile - 3 of price : " , np.percentile(price , 3))

print("\nMath formulas : ")
print("\nbed square : " , np.square(bed))
print("\nbed squareroot : " , np.sqrt(bed))
print("\nbath power : " , np.power(bath , 2))
print("\nbath abs : " , np.abs(bath))

print("\nArithmatic formulas : ")
addition = bed + bath
print("Addition : " , addition )
subtraction = bed - bath
print("subtracttion : " , subtraction) 
multiplication = bed * bath
print("multipliction : " , multiplication)
division = bed / bath
print("division : " , division)

print("\nTrignomatric formulas : ")
sine_value = np.sin(price)
print("sin : " , sine_value)
cosine_value = np.cos(price)
print("cos : " , cosine_value)
tangent_value = np.tan(price)
print("tan : " , tangent_value)
sineh_value = np.sinh(price)
print("sin : " , sineh_value)
cosineh_value = np.cosh(price)
print("cos : " , cosineh_value)
tangenth_value = np.tanh(price)
print("tan : " , tangenth_value)


print("\nLogrithum formulas : ")
print("natural logrithum value : " , np.log(bed))
print("base10 logrithum value : " , np.log10(bed))

print("\nArrays : ")
D2 = np.array([bed , bath])
print("D2 Array : " , D2)
print("Dimention : " , D2.ndim)
print("Size : " , D2.size)
print("Shape : " , D2.shape)
print("Dtype : " , D2.dtype )

print("\nScilcing : ")
print("Splicing array - D2[:1,:5] : " , D2[:1 , :5])
print("Splicing array - D2[:1,4:15:5] : " , D2[:1 , 4:15:5])

print("\nIndexing : ")
print("Indexing [0,1] : " , D2[0,1])
print("Indexing [0,6] : " , D2[0,6])

print("\nIndexing one my one : ")
for elem in np.nditer(D2):
    print(elem)

print("\nIndexing row by row with index : ")
for index, elem in np.ndenumerate(D2):
    print(index, elem)

print("Rehspae : " , np.reshape(D2 , (2 , 200)))
print("Dimention : " , D2.ndim)
print("Size : " , D2.size)
print("Shape : " , D2.shape)
print("Dtype : " , D2.dtype )

