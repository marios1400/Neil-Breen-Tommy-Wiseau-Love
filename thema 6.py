x = raw_input (" Give the sentense  ")
k = x.split (" ")
r=k[0]
d=r[0]+"argh"
k[0]=r[1: ]
for i in range ( 0 , len(k) , 1):
    k[i]=k[i]+d
for i in  range ( 0 , len(k) , 1 ):
    print k[i]
