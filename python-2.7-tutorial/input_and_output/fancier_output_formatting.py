s='hello,world'
str(s)
repr(s)

for x in range(1,11):
    print repr(x).rjust(2),repr(x*x).rjust(3),
    print repr(x*x*x).rjust(4)

'12'.zfill(5)


print 'We are the {} who say "{}!"'.format('knights','Ni')

print '{0} and {1}'.format('spam','eggs')
print '{1} and {0}'.format('spam','eggs')

print 'This {food} is {adjective}.'.format(food='spam',adjective='absolutely horrible')

#old string formatting
import math
print 'The value of PI is approximately %5.3f.'%math.pi
#3.142