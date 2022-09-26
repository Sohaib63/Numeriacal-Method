def P15():
    def trapezoidal(x0,xn,n):
        h = (xn - x0) / n

        integration = f(x0) + f(xn)
        
        for i in range(1,n):
            k = x0 + i*h
            integration = integration + 2 * f(k)
        
        integration = integration * h/2
        
        return integration

    def f(x):
        b=eval(a)
        return b
        
    print("Use ** as exponential operator instead of ^ .")
    a=input("Enter function:")    
    lower_limit = float(input("Enter lower limit of integration: "))
    upper_limit = float(input("Enter upper limit of integration: "))
    sub_interval = int(input("Enter number of sub intervals: "))

    result = trapezoidal(lower_limit, upper_limit, sub_interval)
    print("Integration result by Trapezoidal method is: %0.6f" % (result) )