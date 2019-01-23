sum(i*i for i in range(10))

xvec=[10,20,30]

yvec=[7,5,3]

sum(x*y for x,y in zip(xvec,yvec))

from math import pi,sin
sin_table=dict((x,sin(x*pi/180)) for x in range(0,91))

unique_words=set(word for line in page for word in line.split())

# valedictorian=max((student.gpa,student.name) for student in graduates)



