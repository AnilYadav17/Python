import time

#print(dir(time))
print("\n",time.time())  #-> Seconds since 1970


#used is performance measure 
start = time.time()
for i in range(100000):
    pass
end = time.time()
print(end-start)     #-> Print the time taken by above loop in seconds


#Sleep -> use  to stop a program for given seconds
print("\nHIii")
time.sleep(3)
print("\nHii after 3 seconds\n")

#Time into readable format
print(time.ctime())  #-> Day Month Date Time Year

#if argument given -> Seconds
print(time.ctime(1782678388.2923417))  


#localtime
print(time.localtime())   #->Retuns struct_time object.
#for indidual
x = time.localtime()
print(x.tm_mday)


#utc time
print(time.gmtime())

#imp
'''time.time()
time.sleep()
time.ctime()
time.localtime()
time.strftime()
time.perf_counter()'''