# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали. 
# Превратите функции в методы класса, а параметры в свойства. 
# Задания должны решаться через вызов методов экземпляра.

class ATM:
    def __init__(self):
        money: int = 0
        counter: int = 0
        self.money = money
        self.counter = counter

    def withdraw(self, amount: int) -> None:
        self.counter += 1
        if amount < self.money + self.percentage(amount, -1):
            if amount > 5_000_000:
                self.money -= self.percentage(amount, -1)
            if self.check_if_valid_sum(amount):
                if self.counter < 3:
                    self.money -= amount + self.percentage(amount, self.counter)
                else:
                    self.money -= amount + self.percentage(amount, self.counter)
            else:
                print("Error! Amount must be a multiplicity of 50.")
        else:
            print("Error! You can not withdraw more money than you have on your account.")

    def deposit(self, amount: int) -> None:
        self.counter += 1
        if amount > 5_000_000:
            self.money -= self.percentage(amount, -1)
        if self.check_if_valid_sum(amount):
            if self.counter < 3:
                self.money += amount - self.percentage(amount, self.counter)
            else:
                self.money += amount - self.percentage(amount, self.counter)
        else:
            print("Error! Amount must be a multiplicity of 50.")

    def account(self) -> None:
        print(f"Your account has: {self.money}")

    def core(self) -> None:
            while True:
                self.account()
                match str(input("To deposit money enter 1.\n"
                        "To withdraw money enter 2.\n"
                        "To stop working with the ATM enter 3.\n")):
                    case "1":
                        try:
                            amount = int(input("Please insert money into the ATM.\n"))
                        except ValueError:
                            print("Error!\nPlease insert the money correctly.")
                        self.deposit(amount)
                    case "2":
                        try:
                            amount = int(input("Please enter amount of money to withdraw.\n"))
                        except ValueError:
                            print("Error!\nPlease enter correct data the money correctly.")
                        self.withdraw(amount)
                    case "3":
                        break
                    case _:
                        print("No such operation found!\nPlease try again.")

    @staticmethod
    def percentage(amount: int, check: int = 0) -> float:
        per: float = 1.0
        if check < 3:
            per = 1.5
            if (per * amount) / 100 < 30:
                per = 30
            elif (per * amount) / 100 > 600:
                per = 600
        elif check == -1:
            per = 10.0
            per = (per * amount) / 100
        else:
            per = 3.0
            if (per * amount) / 100 < 30:
                per = 30
            elif (per * amount) / 100 > 600:
                per = 600
        return per

    @staticmethod
    def check_if_valid_sum(amount: int) -> bool:
        return True if amount % 50 == 0 else False


def main():
    amount: int = 0
    atm = ATM()



if __name__ == "__main__":
    atm = ATM()
    atm.core()
