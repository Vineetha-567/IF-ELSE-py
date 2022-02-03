# week nbr
a= int(input("enter nbr :"))
if a==1:
    print("sunday")
elif a==2:
    print("monday")
elif a==3:
    print("tuesday")
elif a==4:
    print("wednesday")
elif a== 5:
    print("thursday")
elif a== 6:
    print("friday")
elif a==7:
    print("saturday")
elif a>=8 and a<=31:
    print("week days only 7days.. check onece your input","\U0001F644")
else:
    print("sorry","\U0001F600","we can't find week nbr","\U0001F632")
