from homework_animal import Animal


class Cat(Animal):

    def __init__(self, name, color, age, sex):
        self.hair = "short"
        super().__init__(name, color, age, sex)

    def catch_rat(self):
        print("它会抓老鼠")

    def animal_call(self):
        print("还会喵喵叫")


if __name__ == '__main__':
    cat = Cat("Tom", "白色", 3, "girl")
    cat.catch_rat()
    cat.animal_call()
