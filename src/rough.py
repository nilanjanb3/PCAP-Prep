class Person():
    def __init__(self,name) -> None:
        self.name = name

    def __str__(self):
        return self.name
    
p1 = Person("Nilanjan")

print(p1)