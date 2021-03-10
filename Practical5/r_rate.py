# we need a sign to represent the number of student while the rate is r. we also need another sign to note the round.
a = 84
r = 1.1
n = 1
# the infection can be culculated by while-loop.
while n <= 5 :
 a = a + a*r
 n = n+1
# finally, print the result.
a = str(a)
r = str(r)
print ("as the r = "+ r)
print ("the number of infected people is "+ a)

