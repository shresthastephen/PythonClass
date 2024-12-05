#Tuples

class A:
    def Sum (self,*arg):
        re=0
        for x in arg:
            re += x
            print(re)
    
result=A()
result.Sum (1,2)
result.Sum (1,2,3)
