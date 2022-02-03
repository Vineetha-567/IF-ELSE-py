# find month days
a=int(input("enter month nbr :"))
if a==31:
    print("This months are having 31 days :")
    print("January")
    print("march")
    print("may")
    print("July")
    print("August")
    print("October")
    print("December")
elif a==29 or a==28:
    print("february")
elif a==30:
    print("this months are having 30 days :")
    print("april")
    print("June")
    print("September")
    print("November")
else:
    print("none")
