class A:
    def Sum (self,a,b,c=0):
        return a+b+c
    
d=A()
print(d.Sum (1,2))
print(d.Sum (1,2,3))
