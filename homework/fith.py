# 1.5 Доработайте задачу.
#     Вынесите общие свойства и методы классов в класс
#     Животное.
#     Остальные классы наследуйте от него.
#     Убедитесь, что в созданные ранее классы внесены правки.

class Animal:
    
    def __init__(self, name: str, say: str, legs: int = 4) -> None:
        self._name = name
        self._say = say
        self._legs = legs
    
    def says(self) -> str:
        return self._say
    
    def has_legs(self) -> bool:
        if self._legs != 0:
            return True
        return False
    
    def name_is(self) -> str:
        return self._name


class Snek(Animal):
    
    def __init__(self, poisonous: bool = False, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._poisonous = poisonous
    
    def poisonous(self) -> bool:
        return self._poisonous
    

class Pig(Animal):
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
    def likes_dirt(self) -> bool:
        return True


class Fish(Animal):
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    
    def swims(self) -> bool:
        return True


if __name__ == "__main__":
    pig = Pig("Oinkers", "Oink-Oink")
    print(f"{pig.has_legs() = }\n{pig.likes_dirt() = }\n{pig.name_is() = }\n{pig.says() = }")
    snek = Snek(True, "Black mamba", "Sssssssssssss",  0)
    print(f"{snek.has_legs() = }\n{snek.poisonous() = }\n{snek.name_is() = }\n{snek.says() = }")
    shark = Fish("White Shark", "Bluub-bluub", 0)
    print(f"{shark.has_legs() = }\n{shark.swims() = }\n{shark.name_is() = }\n{shark.says() = }")
