# chk lower or upper or digit or nbr
a= int (input("enter  nbr:"))
if  a >=0 and a<=9: 
    print("digit")
if a>=10 and a<= 999:
    print("numbers")
chr= input("enter chr :")
if chr >"A" and chr< "Z":
    print("upper case")
elif chr > "a" and chr < "z":
    print("lower case")
else:
    print("special character")