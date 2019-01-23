while True:
    try:
        x=int(raw_input("please enter a number:"))
        break
    except ValueError:
        print "Oops! That was no valid number. Try again..."

#except (RuntimeError,TypeError,NameError):
    #pass

import sys
try:
    f=open('myfile.txt')
    s=f.readline()
    i=int(s.strip())
except IOError as e:
    print "I/O error({0}):{1}".format(e.errno,e.strerror)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexpected error:",sys.exc_info()[0]
    raise

# for arg in argv[1:]:
#     try:
#         f=open(arg,'r')
#     except IOError:
#         print 'cannot open',arg
#     else:
#         print arg,'has',len(f.readline()),'lines'
#         f.close()

# try:
#     raise Exception('spam','eggs')
# except Exception as inst:
#     print type(inst)
#     print inst.args
#     print inst
#     x,y=inst.args
#     print 'x=',x
#     print 'y=',y
# <type 'exceptions.Exception'>
# ('spam','eggs')
# ('spam','eggs')
# x=spam
# y=eggs