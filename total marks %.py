# total marks %10
print("enter the marks of five subjects ::")
a=int(input("physics :"))
b=int(input("chemistry :"))
c=int(input("biology :"))
d=int(input("mathematics :"))
e=int(input("computer :"))
# it will calcuate the total ,average & percentage
total= a+b+c+d+e
average= total/5
percentage =(total/500.0)*100
if average >= 90:
    grade="A"
elif average >=80 and average <90:
    grade="B"
elif average >=70 and average <80:
    grade="C"
elif average >=60 and average <70:
    grade="D"
else:
    grade ="E"
#  it will produce the final output
print("\n the total marks is :\t",total,"/500")
print("\n the average marks is :\t",average)
print("\n the percentage is :\t",percentage,"%")
print("\n the grade is :\t",grade)