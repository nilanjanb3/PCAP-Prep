class A:
    def add(self,a,b):
        return a+b
class B(A):
    # pass
    def add(self,a,b,c = 0,d = 0): # Polymorphism (Method Overloading & Method Overriding)
        return super().add(a,b)+c+d
    
        

b = B()

print(b.add(1,2))
print(b.add(1,2,3))
print(b.add(1,2,3,4))