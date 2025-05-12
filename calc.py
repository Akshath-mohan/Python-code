### wap to define the calculator methods like addition ,subs,divison,mult using lambda function
#in a class name as calculator

class calc:
    a=print(input("enter the value of a = "))
    b=print(input("enter the value of b = "))
    x=print(input("enter the value of x = "))
    y=print(input("enter the value of y = "))
    add = lambda x,y,a,b: x+y+a+b
    sub = lambda x,y,a,b: x-y-a-b
    mul = lambda x,y,a,b: x*y*a*b
    div = lambda x,y,a,b: x/y/a/b
    print="github desktop"



obj=calc
print(obj.add())
print(obj.sub())
print(obj.mul())
print(obj.div())
