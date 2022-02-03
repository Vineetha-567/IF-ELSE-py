a=int(input("enter age :"))
b=(input("enter sex :"))
c=int(input("enter no of days :"))
if a>=18 and a<30:
    if b== "male":
        print(c*700)
    elif b== "female":
        print(c*750)
elif a>30 and a<=40:
    if b== "male":
        print(c*800)
    elif b== "female":
        print(c*850)
else:
    print("approprite age")
