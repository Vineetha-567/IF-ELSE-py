# chek type of triangle
x=int(input("enter num :"))
y=int(input("enter num :"))
z=int(input("enter num :"))
if x==y==z:
    print("equal triangle")
elif x==y or y==z or z==x:
    print("isosceles triangle")
else:
    print("scalene triangle")