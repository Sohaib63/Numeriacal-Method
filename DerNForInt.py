def P4():    
    degree=0
    values=0
    actual_degree=0
    xp=0
    h=0
    p=-2
    delta=[0,0,0,0,0,0,0,0,0,0]
    x=[]
    fx=[]
    class NewForwDiff:
        def __init_(self):
            print("\n\t\tFROM NEWTON'S FORWARD DIFFERENCE FORMULA\n\n")

        def result(self):
            print("How many values you want for x?\t")
            values=int(input())
            print("Upto what power of Delta:\t")
            degree=int(input())
            print("\n Value of Xp:\t")
            xp=float(input())

            for i in range(values):
                print("\nEnter X"+str(i+1)+":\t")
                x.append(float(input()))
                print("Enter F("+str(i+1)+"):\t")
                fx.append(float(input()))
            print("\nX\t",end=" ")
            for i in range(values):
                print("\t",x[i],end=" ")
            print("\n")
            print("\nF(x)\t",end=" ")
            for i in range(values):
                print("\t",fx[i],end=" ")
            print("\n")
            p=-2
            h=x[1]-x[0]
            temp=-1
            for j in range(values):
                if (p<0 or p>1):
                    p=(xp-x[j])/h
                    temp=j         
            print("\nValue of P is :\t",p,"\n")
            j=values
            for actual_degree in range(1, (degree+1)):
                if (j>1):
                    print("\n\nDelta power",actual_degree,":\t",end=" ")
                    for k in range(j-1):
                        fx[k]=fx[k+1]-fx[k]
                        print(fx[k],"\t",end=" ")
                    delta[actual_degree-1]=fx[temp]
                    #print(delta[actual_degree-1])
                    j-=1
        
            parray1=[1,2*p-1,3*p*p-6*p+2,4*p*p+18*p*p+22*p-6]
            div1=[1,2,6,24]
            ans1=0
            for i in range(actual_degree):
                ans1+=delta[i]*parray1[i]/div1[i]
            print("\n\n\nf`(",xp,"):\t",(ans1/h))

            parray2=[1,p-1,6*p*p-18*p+11]
            div2=[1,1,12]
            ans2=0
            for i in range(1,actual_degree):
                ans2+=delta[i]*parray2[i-1]/div2[i-1]
            print("\n\n\nf``(",xp,"):\t",ans2/(h*h))


    obj=NewForwDiff()
    obj.result()


