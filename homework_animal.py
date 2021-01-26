"""
比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
重写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法，改成【喵喵叫】

"""


class Animal:

    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex
        print(f"我有一只宠物名叫：{self.name}, 他是{self.color}的，今年{self.age}岁了，是个{self.sex}")

    def animal_call(self):
        print("动物会叫")

    def animal_run(self):
        print("动物会跑")


if __name__ == '__main__':
    animal = Animal("tom", "白色", 3, "male")
