class Rectangle:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return f"Rectangle {self.a}x{self.b} = "
    def area(self):
        return self.a*self.b

class Square:
    def __init__(self,a):
        self.a=a
    def __str__(self):
        return f"Square {self.a}x{self.a} = "
    def area(self):
        return self.a**2

class Circle:
    def __init__(self,r):
        self.r=r
    def __str__(self):
        return f"Circle radius {self.r} = "
    def area(self):
        return 3.14*self.r**2


