from math import sin,cos,tan,sinh,cosh,tanh
def P5():
    def f(x,y):
        b=eval(a)
        return b

    def euler(x0,y0,xn,n):
        h = (xn-x0)/n
        
        print('\n-----------SOLUTION-----------')
        print('------------------------------')    
        print('x0\ty0\tslope\tyn')
        print('------------------------------')
        for i in range(n):
            slope = f(x0, y0)
            yn = y0 + h * slope
            print('%.4f\t%.4f\t%0.4f\t%.4f'% (x0,y0,slope,yn) )
            print('------------------------------')
            y0 = yn
            x0 = x0+h
        
        print('\nAt x=%.4f, y=%.4f' %(xn,yn))

    print("Use ** as exponential operator instead of ^ .")
    a=input("Enter function:\t")

    print('Enter initial conditions:')
    x0 = float(input('x0 = '))
    y0 = float(input('y0 = '))

    print('Enter calculation point: ')
    xn = float(input('xn = '))

    step = int(input('Enter number of steps:'))

    euler(x0,y0,xn,step)
