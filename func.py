#function without parameter and with return
def add():
    a=10
    b=15
    a=a+b
    print("Addition is",a)

add( )

#function with parameter and without return
def sub(a,b):
    a=a-b
    print("Substraction is",a)
    
sub(15,5)   

#function without parameter and with return
def multi(n1,n2):
    return n1*n2
res=multi(25,6)
print("The multiplication is",res)