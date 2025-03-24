
"""
class Dog:  # 定义名称
    def __init__(self, name, age, weight, colour,):  # 定义属性name和age和weight和colour
        self.name = name#调用参数
        self.age = age
        self.weight = weight
        self.colour = colour

#类方法，名字中定义名字（关键名）
    def sit(self):
        print(f'{self.name}is now sitting.')

    def roll_over(self):
        print(f'{self.name} rolled over!')

    def speak(self):
        print(f"{self.weight}is this my weight.")

    def see(self):
        print(f"the{self.colour}is my colour.")

    def eat(self,food):
        print(f"my dog eat {food}")
#实体化打印
my_Dog = Dog('Willie', 6, "79kg", "red")
print(f"My dog's name is {my_Dog.name}.")
print(f"My dog is {my_Dog.age} years old.")
print(f"My dog weight is {my_Dog.weight}")
print(f"My dog colour is{my_Dog.colour}")
print(f"My dog eat{my_Dog.eat}")
#打印关键名
my_Dog.sit()
my_Dog.roll_over()
my_Dog.speak()
my_Dog.see()
my_Dog.eat(food="shit")
"""
"""
class car:
    def __init__(self,make,year,model):
        self.make = make
        self.year = year
        self.model = model

    def get_descriptive_name(self):
        #返回格式规范的描述性信息
        long_name = f"{self.year}{self.make}{self.model}"
        return long_name.title()
my_new_car = car('奥迪','2024','a4')
print(my_new_car.get_descriptive_name())

class Electriccar(car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)

    def get_descriptive_name(self):
        print('子类的描述方法')

my_leaf = Electriccar('nissan','2024','leaf')
print(my_leaf.get_descriptive_name())
"""


