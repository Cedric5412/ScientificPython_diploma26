class complex:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self,other):   
        x = self.x + other.x
        y = self.y + other.y
        return complex(x,y)
    
    def __substr__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return complex(x,y)
    
    def __times__(self, other):
        x = self.x * other.x - self.y * other.y
        y = self.y * other.x + self.x * other.y
        return complex(x,y)
    
    def __div__(self, other):
        denom = (other.x)**2 - (other.y)**2
        if denom == 0:
            return
        x = (self.x * other.x + self.y * other.y) / denom
        y = (self.y * other.x - self.x * other.y) / denom
        return complex(x, y)

    def __str__(self):
        return "z = {0} + {1}j".format(self.x, self.y)
    

z1 = complex(1, 1)
z2 = complex(2, 0)
print(z1.__add__(z2))
print(z1.__substr__(z2))
print(z1.__times__(z2))
print(z1.__div__(z2))
        