from sympy import Symbol, Derivative
def P10():
    x= Symbol('x')
    print("Use ** as exponential operator instead of ^ .")
    a=input("Enter function:")
    b=eval(a)
    deriv= Derivative(b, x)


    def f(x):
        bc=eval(a)
        return bc

    def g(y):
        return deriv.doit().subs({x:y})

    def newtonRaphson(x0,e,N):
        print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
        step = 1
        flag = 1
        condition = True
        while condition:
            if g(x0) == 0.0:
                print('Divide by zero error!')
                break
            
            x1 = x0 - f(x0)/g(x0)
            #print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
            x0 = x1
            step = step + 1
            
            if step > N:
                flag = 0
                break
            
            condition = abs(f(x1)) > e
        
        if flag==1:
            print('\nRequired root is: %0.8f' % x1)
        else:
            print('\nNot Convergent.')


    x0 = float(input('Enter Guess: '))
    e = float(input('Tolerable Error: '))
    N = int(input('Maximum Step: '))

    newtonRaphson(x0,e,N)