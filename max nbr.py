# print max nbr
a=int(input("enter a nbr :"))
b=int(input("enter a nbr :"))
c=int(input("enter nbr :"))
if b<a<c:
    print(a,"is max")
elif a<b>c :
    print(b," is max")
elif b<c>a:
    print(c,"is max")
else:
    print("equal")