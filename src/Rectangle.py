from Figure import Figure


class Rectangle(Figure):
    def __init__(self, RectSideA, RectSideB):
        if RectSideA <= 0 or RectSideB <= 0:
            raise ValueError("Сторона прямоугольника должна быть больше нуля")
        self.RectSideA = RectSideA
        self.RectSideB = RectSideB

    @property
    def get_perimeter(self):
        return (self.RectSideA + self.RectSideB) * 2
    
    @property
    def get_area(self):
        return self.RectSideA * self.RectSideB
    


RectEx1 = Rectangle(2, 5)
RectEx2 = Rectangle(3, 8)

print(f" Периметр RectEx1 равен {RectEx1.get_perimeter}")
print(f" Площадь RectEx1 равна {RectEx1.get_area}")
print(f" Площадь RectEx2 равна {RectEx2.get_area}")
print(f" Сумма площадей RectEx1 и RectEx2 равна {RectEx2.add_area(RectEx1)}")