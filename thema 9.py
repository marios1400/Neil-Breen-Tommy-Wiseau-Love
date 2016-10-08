x = raw_input ("Give the number  ")
b = len(x)
A = []
d=0
c=1
for i in range (0 , b ,1):
    A.append(x[i])
while (len(A) > 1):
    c=1
    for i in range (0 , len(A) ,1):
        c=int (A[i]) *c
    d=d+1
    c=str(c)
    while len(A)>0:
        A.pop()
    for i in range (0 , len(c) , 1 ):
        A.append(c[i])
print d
