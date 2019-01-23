import zlib
s='witch which has which witches wrist watch'
print s
len(s)

t=zlib.compress(s)

# print t

len(t)

print len(t)

zlib.decompress(t)

zlib.crc32(s)