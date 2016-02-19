import math
x = math.pi / 4
val = (math.sin(x)**2) + (math. cos(x)**2)
print val


v0 = 3 #m/s
t = 1 #second
a = 2**2 #m/s
s = (v0 * t) + (((a) * t ** 2) / 2)
print s



a = 3.3
b = 5.3
a2 = a**2
b2 = b**2
eq1sum = a2 + (2 * a * b) + b2
eq2sum = a2 - (2 * a * b) + b2
eq1pow = (a + b)**2
eq2pow = (a - b)**2
print 'eq1sum' , eq1sum
print 'eq2sum' , eq2sum

print 'eq1pow' , eq1pow
print 'eq2sum' , eq2sum
