# strog password
print("password")
a= (input("enter uppercase :"))
b= (input("enter lowerrcase :"))
c= (input("enter special chtr :"))
d= int(input("enter digit :"))
if a>= "A" and a<= "Z":
    if b>= "a" and b<= "z":
        if d>= 0 and d<= 9:
            if  c in "@""#""$""%""&""^""*""!":
                print(a+b+c+str(d)+c+str(d)+b+c+a)

