from cmath import sin


h=int(input("enter a hight:"))
a=int(input("enter a angle:"))
pie=(3.14)
algler=((pie/180)*a)
l=(h/sin(algler))
print("ladder lanth :",l)
