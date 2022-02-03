# class allowed or not
a=int(input("enter class held :"))
b=int(input("enter class attendance :"))
c= b*100/a
if c >75:
    print("allow to class")
else:
    print("not allowed")