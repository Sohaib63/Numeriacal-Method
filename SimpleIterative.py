from math import sin,cos,tan,sinh,cosh,tanh
def P14():
    def f(x):
        b=eval(a)
        return b

    i=1
    n=1
    flag=1
    x2=0.0
    ch=" "
    e=0.0
    x0=0.0
    x1=0.0

    print("\n\n\tSIMPLE ITERATIVE METHOD")
    print("\tUse ** as exponential operator instead of ^ .")
    a=input("\tEnter function:\t") 
    print("\n\tEnter value of X0:\t",end=" ")
    x0=float(input())
    print("\n\tEnter value of N:\t",end=" ")
    n=int(input())
    print("\n\tEnter value of E:\t",end=" ")
    e=float(input())

    x1=f(x0)

    for i in range(n):
        if (flag==1):
            x2=x1-x0
            if (x2<0):
                x2=x2*(-1)
                if (x2<e):
                    flag=0
                else:
                    x0=x1
                    x1=f(x0)

    if (flag==0):
        print("\n\n\tNo convergence")
    else:
        print("\n\nAfter\t",i,"\tIterations, Root is\t",x1)