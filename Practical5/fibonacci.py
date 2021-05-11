# we need a value called n to note the place. And we should start from 1, 1.
a = 1
b = 1
c = a+b
n = 2
print(a)
print(b)
# then we should do a circulation 
while n < 13:
# in the process, a and b should be update, and a new sign to calculate a+b
 if n%2 == 1 :
  c = a + b
  b = c
  n = n+1
  print(c)
 else:
  c = a + b
  a = c
  n = n+1
  print(c)
# as n = 13, the circulation should be stopped.

