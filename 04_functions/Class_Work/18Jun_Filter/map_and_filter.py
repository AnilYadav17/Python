'''l = [1,2,3,4]

r = map(lambda x:x**2 ,l)
l =  list(r)
r =  filter(lambda x:x%2==0,l)

print(list(r))'''
#r = fiter(lamda x:x%2==0,map(lambda a:a*a,l1))



l = [1,2,3,4,5]

print(list(map(lambda x:x*x,
	filter(lambda x:x%2==0,l ))))
