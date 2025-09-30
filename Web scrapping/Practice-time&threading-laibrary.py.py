#This file is to practice tine and threding libbary a little as i am tryng to leran attaching proxyies with
# webscappping

import time
import threading



def func(sec): # a funtion that is accepting the sec we want it to wait
    print(f"This is print at {sec} : ") # it will be printes first then
    time.sleep(sec) # this is a method of time librray at it make the compiler sleep after the pervous line 

time_taken_from_1st_to_6th_line = time.perf_counter()

func(4)
## after this the compiler will wait till 4 sec 
func(2)
func(5)
time_taken_from_1st_to_13th_line = time.perf_counter()
# this is the way too actually knowing how much time it too to compile till now 

# so for this code it will show the time it took ffrom the line one which is 333972.6748907 secs how ever we we want to know that how
# time it took after fun(4) meaning runing the function it should takke arouf 11 sec . lets minuce the time take till 6th line to time taken till 14th 

print("time taking without threads " ,time_taken_from_1st_to_13th_line - time_taken_from_1st_to_6th_line)

# noe starting threadings 
# since python run line by line we need it to run ecah line parallet for that we wil use thread
# we are going to convert line 11 , 13 , 14 into threads as it will then be running parallel

print("          Starting threads : ")

t1 = threading.Thread(target=func , args=[4]) # same as calling a function like func(4)
t2 = threading.Thread(target=func , args=[2]) # same as like func(2)
t3 = threading.Thread(target=func , args=[5]) # same as like func(5)

# now we must know some methods of threads are start() to start the thread. and a join() to compelete the thread before returning
time_taken_from_1st_to_34th_line = time.perf_counter()
t1.start()
t2.start()
t3.start()
time_taken_from_1st_to_38th_line = time.perf_counter()
print("time taking with threads " ,time_taken_from_1st_to_38th_line - time_taken_from_1st_to_34th_line)
