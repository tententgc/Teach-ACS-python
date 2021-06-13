
n1 =int(input("Enter number:"))
n2 =int(input("Enter number:"))
n3 =int(input("Enter number:"))
n4 = n1*n2*n3

def find_lcm(n1,n2,n3,n4): #ครน.
    for i in range(1,(n4+1)):
        if i% n1 ==0 and i% n2==0 and i% n3==0:
            return(i)
def find_gcd(n1,n2,n3):#หรม
    if n1> n3:
        n1,n3 =n3,n1
    elif n1>n2:
        n1,n2 = n2,n1
    for i in range(n1,0,-1):
        if n1%i == 0 and n2%i==0 and n3%i==0:
            return (i)
lcm=find_lcm(n1,n2,n3,n4)
gcd=find_gcd(n1,n2,n3)
if n4== lcm*gcd:
    print("Absolutly Yes")
else:
    print ("Absolutly NO")

