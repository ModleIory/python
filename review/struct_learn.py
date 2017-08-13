import struct

print('struct to support binary')

a = 1234887
out = struct.pack('i',a)
print(out)