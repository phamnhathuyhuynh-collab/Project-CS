class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height 
        
    def set_width(self, width):
        self.width = width
        return self.width
    
    def set_height(self, height):
        self.height = height
        return self.height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2*self.width + 2*self.height
    
    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5
    
    def get_picture(self):
        picture = ""
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        for _ in range(self.height):
            for _ in range(self.width):
                picture += '*'
            picture += '\n'
        return picture

    def get_amount_inside(self, other_shape):
        if min(self.width // other_shape.width, self.height // other_shape.height) == 0:
            return 0
        return self.width // other_shape.width *self.height // other_shape.height
    
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
            


class Square(Rectangle):#cach lam cua to

    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def set_side(self, side_new):
        Rectangle.set_height(self, height=side_new)
        Rectangle.set_width(self, width=side_new)
        self.side = side_new
        
    def set_height(self, side1):
        super().set_height(side1)
        self.side = side1
        return self.side
   
    def set_width(self, side2):
        super().set_width(side2)
        self.side = side2
        return self.side
    
    def __str__(self):
       return f'Square(side={self.side})'

class Square(Rectangle):#cach lam khac nhung van dung 
    def __init__(self, side):
        super().__init__(side, side)
        
    def set_height(self, side):
        self.height = side
    
    def set_width(self, side):
        self.width = side
        
    def set_side(self, side):
        self.height = side
        self.width = side
    
    def __str__(self):
        return f'Square(side={self.width})'
    


rect = Rectangle(5, 55)
print(rect.get_area())
rect.set_height(55)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(55)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())
sq.set_height(3)
print(sq)

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))