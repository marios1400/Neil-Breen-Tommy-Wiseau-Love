import math 
a = input ("Give the first number : ")
b = input ("Give the second number : ")
c = input ("Give the third number : ")
if (math.fabs(c-b)<a and a<b+c):
    if (a>b and a >c):
        if (a*a==b*b+c*c):
            print ("3")
        elif (a*a>b*b+c*c):
            print("2")
        elif (a*a<b*b+c*c):
            print ("1")
    elif (b>a and b>c):
        if (b*b==a*a+c*c):
            print ("3")
        elif (b*b>a*a+c*c):
            print("2")
        elif (b*b<a*a+c*c):
            print ("1")  
    elif (c>a and c>b):
        if (c*c==b*b+a*a):
            print ("3")
        elif (c*c>b*b+a*a):
            print("2")
        elif (c*c<b*b+a*a):
            print ("1")
    elif (a==b and a==c):
        print ("1")
else:
    print ("-1")
