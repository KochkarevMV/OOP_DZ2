from Figure import Figure
import math


class Circle(Figure):
    def __init__(self, circleRadius):
        if circleRadius <= 0:
            raise ValueError("Радиус круга должен быть больше нуля")
        self.circleRadius = circleRadius

    @property
    def get_perimeter(self):
        circlePerimetr = math.trunc(2*math.pi*self.circleRadius)
        return circlePerimetr
    
    @property
    def get_area(self):
        circleArea = math.trunc(math.pi*(self.circleRadius**2))
        return circleArea
    

Circle1 = Circle(7)
Circle2 = Circle(5)

print(f" Периметр Circle1 равен {Circle1.get_perimeter}")
print(f" Площадь Circle1 равна {Circle1.get_area}")
print(f" Площадь Circle2 равна {Circle2.get_area}")
print(f" Сумма площадей Circle1 и Circle2 равна {Circle1.add_area(Circle2)}")