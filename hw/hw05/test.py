from hw05 import *

seq = [1,2]
a = perms(seq)
b = [next(a) for i in seq]
print(b)