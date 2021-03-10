a = 120901
b = 190784
c = 100321
d = abs(a-c)
e = abs(b-c)
if d > e :
 print "d is greater"
elif d == e :
 print "d is equal to e"
else :
 print "e is greater"

X = True
Y = False
Z = (X and not Y) or (Y and not X)
print Z
W = X != Y
print W
