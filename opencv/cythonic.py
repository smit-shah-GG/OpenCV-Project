import cython

a : cdef.float =  0

print(" Enter the number: ")
a = float(input())

print("The number is" + a)