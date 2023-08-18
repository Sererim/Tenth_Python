# 1.1 Создайте класс окружность.
#     Класс должен принимать радиус окружности при создании
#     экземпляра.
#     У класса должно быть два метода, возвращающие длину
#     окружности и её площадь.

class Circle:
    
    _pi: float = 3.141592654
    
    def __init__(self, radius: float) -> None:
        self.radius = radius
    
    def circumference(self) -> float:
        return (2 * self._pi * self.radius).__round__(3)
    
    def area(self) -> float:
        return (self._pi * (self.radius)**2).__round__(3)
    

if __name__ == "__main__":
    round = Circle(10)
    print(f"{round.circumference() = }")
    print(f"{round.area() = }")
