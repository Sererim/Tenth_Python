# 1.3 Напишите класс для хранения информации о человеке:
#     ФИО, возраст и т.п. на ваш выбор.
#     У класса должны быть методы birthday для увеличения
#     возраста на год, full_name для вывода полного ФИО и т.п. на
#     ваш выбор.
#     Убедитесь, что свойство возраст недоступно для прямого
#     изменения, но есть возможность получить текущий возраст.

class Person:
    
    def __init__(self, first_name: str, second_name: str, family_name: str, age: int) -> None:
        self.__first_name = first_name
        self.__second_name = second_name
        self.__family_name = family_name
        self.__age = age
    
    def full_name(self) -> str:
        return f"{self.__family_name} {self.__first_name} {self.__second_name}"
    
    def birthday(self):
        self.__age += 1
    
    def get_age(self) -> int:
        return self.__age
    
    
if __name__ == "__main__":
    man = Person("Null", "Nullovich", "Nullov", 20)
    print(man.full_name())
    print(man.get_age())
    print(man.birthday())
    print(man.get_age())
    # print(man.__age)
 