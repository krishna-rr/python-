a=int(input("enter a 1th number:-"))
b=int(input("enter a  2th number :-"))
c=int(input("enter a 3th number :-"))
j=(a if(a>b and a>c) else b if(b>a and b>c)else c)
print("maxmum number is :-",j)

