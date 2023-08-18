# 2. Доработаем задания 5-6. Создайте класс-фабрику.
#  2.1 Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
#  2.2 Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.


class Being:
    
    def __init__(self, name: str, say: str, legs: int = 4, type="Pig") -> None:
        self._name = name
        self._say = say
        self._legs = legs
        self._type = type
    
    def says(self) -> str:
        return self._say
    
    def has_legs(self) -> bool:
        if self._legs != 0:
            return True
        return False
    
    def name_is(self) -> str:
        return self._name

    def factory(self):
        if self._type == "Fish":
            return Fish(self._name, self._say, self._legs)
        elif self._type == "Snek":
            return Snek(self._name, self._say, self._legs)
        elif self._type == "Pig":
            return Pig(self._name, self._say, self._legs)
        else:
            return None
    

class Snek(Being):
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._poisonous = False
    
    def is_poisonous(self, poison: bool) -> None:
        self._poisonous = poison
        
    def poisonous(self) -> bool:
        return self._poisonous
    

class Pig(Being):
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
    def likes_dirt(self) -> bool:
        return True


class Fish(Being):
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    
    def swims(self) -> bool:
        return True


if __name__ == "__main__":
    obj = Being(name="Python", say="SSSssss", legs=0, type="Snek").factory()
    print(obj.name_is())
    # obj.likes_dirt() 'Snek' object has no attribute 'likes_dirt'
    obj.is_poisonous(False)
    print(f"{obj.name_is() = }\n{obj.has_legs() = }\n{obj.poisonous()}")
    obj2 = Being(name="Oinkers", say="Oink-oink", type="Pig").factory()
    print(f"{obj2.name_is() = }\n{obj2.has_legs() = }\n{obj2.likes_dirt()}")
