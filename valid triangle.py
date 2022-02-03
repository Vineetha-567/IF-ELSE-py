# chl valid triangle or nt
a=int(input("enter length of side a :"))
b=int(input("enter length of side b :"))
c=int(input("enter length of side c :"))
if a+b >=c and b+c >=a and c+a>=b:
    print("valid traiangle")
else:
    print("not valid")