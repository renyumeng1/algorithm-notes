#原理gcd(F2020,F520)==F(gcd(2020,520))
def gcd(a,b):
    if b==0:return a
    else:return gcd(b,a%b)
def fi(n):#dp
    if n <= 2:
        return 1
    pre = 1
    sur = 1
    for i in range(3,n+1):
        pre,sur = sur,pre+sur
    return sur
print(fi(gcd(2020,520)))
