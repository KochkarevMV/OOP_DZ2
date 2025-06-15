from Figure import Figure
import math


class Triangle(Figure):
    def __init__(self, triA, triB, triC):
        if triA <= 0 or triB <= 0 or triC <= 0:
            raise ValueError("Длина сторон должна быть больше нуля")
        if triA + triB == triC or triA + triC == triB or triB + triC == triA:
            raise ValueError("Сумма длин двух сторон треуголника не должна быть равна длине третьей стороны")
        if triA + triB < triC or triA + triC < triB or triB + triC < triA:
            raise ValueError("Сумма длин двух сторон треуголника не должна быть меньше длины третьей стороны")
        self.triA = triA
        self.triB = triB
        self.triC = triC
        
    @property
    def get_perimeter(self):
        return self.triA + self.triB + self.triC

    @property
    def get_area(self):
        triP = (self.triA + self.triB + self.triC)/2
        triS = math.trunc(math.sqrt(triP*(triP-self.triA)*(triP-self.triB)*(triP-self.triC)))
        return triS


Tri1 = Triangle(4, 7, 10)
Tri2 = Triangle(4, 3, 2)


print(f" Площадь Tri1 равна {Tri1.get_area}")
print(f" Площадь Tri2 равна {Tri2.get_area}")
print(f" Периметр Tri1 равен {Tri1.get_perimeter}")
print(f" Сумма площадей Tri1 и Tri2 равна {Tri1.add_area(Tri2)}")