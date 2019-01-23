f=open('workfile','r')
print f

f.read()
#input 'This is the entire file.\n'

f.read()
#input ''

f.readline()
#input 'This is the first line of the file.\n'

f.readline()
#input 'This is the second line of the file.\n'

f.readline()
#input ''

f=open('workfile','w')

f.write('This is a test\n')

value=('the answer',42)

s=str(value)

f.write(s)

f=open('workfile','r+')

f.write('012345789abcdef')
f.seek(5)
f.read(1)
#'5'
f.seek(-3,2)
f.read(1)
#'d'