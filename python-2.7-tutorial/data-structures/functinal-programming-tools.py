def f(x): return x%3==0 or x%6==0

def cube(x): return x*x*x

#batch return true params
filter(f,range(2,25))
#return [3,5,6,9,10,12,15,18,20,21,24]

#batch return results
map(cube,range(1,11))
#return [1,8,27,64,125,216,343,512,729,1000]

def add(x,y): return x+y
reduce(add,range(1,11))
#return 55