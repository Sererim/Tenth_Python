# 1.2 Создайте класс прямоугольник.
#     Класс должен принимать длину и ширину при создании
#     экземпляра.
#     У класса должно быть два метода, возвращающие периметр
#     и площадь.
#     Если при создании экземпляра передаётся только одна
#     сторона, считаем что у нас квадрат.

class Rectangle:
    
    def __init__(self, lenght: float, height: float = 0) -> None:
        self.lenght = lenght
        self.height = height
    
    def perimeter(self) -> float:
        if self.height == 0:
            return self.lenght * 4
        return 2 * (self.lenght + self.height)
    
    def area(self) -> float:
        if self.height == 0:
            return self.lenght * self.lenght
        return self.lenght * self.height
    

if __name__ == "__main__":
    abcd = Rectangle(10)
    print(f"{abcd.perimeter() = }\n{abcd.area() = }")
    dcba = Rectangle(10, 5)
    print(f"{dcba.perimeter() = }\n{dcba.area() = }")
