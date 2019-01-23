def f(x):
    return x%3==0 or x%5==0

result1=filter(f,[1,2,3,4,5,6,7,8,9,10])
print result1

def ssquare(x): return x*x

result2=map(ssquare,range(1,6))
print result2

def sum(x,y):return x+y
result3=reduce(sum,range(1,11))
print result3

result4=range(20)
print result4

vec=[-4,-2,0,2,4]
a=[x*2 for x in vec]
print a

print 8**2

b1=[(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
print b1

'''
functin
'''

range(1,10,2)

'''
function
'''

a=0
b=1
while a<=5:
    print a
    a,b=b,a+b

c=range(3,6)
args=[3,6]
c1=range(*args)

'''
    lambda
'''

def make_incremenor(n):
    return lambda x:x+n
f=make_incremenor(42)
kk=f(0)
print kk
kk=f(100)
print kk

'''
get document
'''

def my_function():
    '''Do nothing,but ducument it.

    No,really,it doesn't do anything. 
    '''
    pass
print my_function.__doc__


''' list '''
a=[]
a.append(1)
a.pop()
a.reverse()

t=[1,2,3,4,5]
[z*2 for z in t]

t1=[1,2,3]
t2=[1,2,3]
[(m,n) for m in t1 for n in t2 if m!=n]


'''del statement'''
a=[-1,1,2,3,4,5,6]
del a[0]

del a

'''tuples and sequences'''

t=123,123,"hello"
t[0]

u=t,(1,2,3,4,5)

'''len'''
empty=0
singleton='hello'
len(empty)
len(singleton)


'''Sets  distinct data container'''
basket=['apple','orange','apple','pear','orange','banana']
fruit=set(basket)
'orange' in fruit

''' dictinonary'''
tel={'jack':4098,'sape':4139}
tel['lkx']=6710
tel.keys()
'lkx' in tel
{x: x**2 for x in (2,4,6)}



