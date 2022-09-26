def P7():
    def Convert(string):
        li = list(string.split(" "))
        return li

    print("Just enter coefficients of variables in order and lastly constant using space as delimitor")
    e1=input("Enter equation1: ")
    l1=Convert(e1)
    e2=input("Enter equation2: ")
    l2=Convert(e2)
    e3=input("Enter equation3: ")
    l3=Convert(e3)
    g=input("Enter 3 guesses: ")
    l4=Convert(g)

    a11=int(l1[0])
    a12=int(l1[1])
    a13=int(l1[2])
    aa=int(l1[3])

    a21=int(l2[0])
    a22=int(l2[1])
    a23=int(l2[2])
    bb=int(l2[3])

    a31=int(l3[0])
    a32=int(l3[1])
    a33=int(l3[2])
    cc=int(l3[3])

    g1=int(l4[0])
    g2=int(l4[1])
    g3=int(l4[2])


    def seidel(a, x ,b):
            
        n = len(a)                   
        
        for j in range(0, n):        
            
            d = b[j]                  
            for i in range(0, n):     
                if(j != i):
                    d-=a[j][i] * x[i]
     
            x[j] = d / a[j][j]
        
        return x    
    
                
    n = 3                              
    a = []                            
    b = []        
                 
    x = [g1,g2,g3]                    
    a = [[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]]
    b = [aa,bb,cc]
    
    
    for i in range(0, 25):            
        x = seidel(a, x, b)
        
    print(x)      