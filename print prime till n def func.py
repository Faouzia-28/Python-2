def prime(n):
    
    for i in range(2,n+1):
        flag=0
        for j in range(2,i):
            if i%j==0:
                flag=1
                
        if flag==0:
            print(i)
        
n=int(input("enter a end value"))
prime(n)
            
        
    
