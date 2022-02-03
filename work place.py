# work allow place
a=int(input("enter age :"))
b=input("enter sex :")
c=input("enter marital status :")
if b== "female":
    print("work in urban")
else:
    if b== "male":
        if a>20 and a<40:
            print(" you work any where")
        elif b== "male":
            if a>40 and a<60:
                print("you work only urban")
            else:
                print("age error")