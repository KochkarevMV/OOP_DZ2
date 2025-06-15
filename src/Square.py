from Figure import Figure
    

class Square(Figure):
    def __init__(self, square_sideA):
        if square_sideA <= 0:
            raise ValueError("Сторона квадрата должна быть больше нуля")
        self.square_sideA = square_sideA

    @property
    def get_perimeter(self):
        return self.square_sideA*4
    
    @property
    def get_area(self):
        return self.square_sideA*self.square_sideA
    

SquareEx = Square(5)
SquareEx2 = Square(2)

print(f" Периметр SquareEx равен {SquareEx.get_perimeter}")
print(f" Площадь SquareEx равна {SquareEx.get_area}")
print(f" Площадь SquareEx2 равна {SquareEx2.get_area}")
print(f" Сумма площадей SquareEx и SquareEx2 равна {SquareEx2.add_area(SquareEx)}")
