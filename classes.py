# >>>>> Classes <<<<<
class Point:
    # __init__ function is constructor of the class
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('Move the Point')

    def draw(self):
        print('Draw the Point')


point1 = Point()
point1.x = 1
point1.y = 3
print(point1.x, point1.y)
point1.move()
point1.draw()

Point2 = Point
print(Point2)
point3 = Point2()
print(point3)


point4 = Point(3, 5)
print(point4.x, point4.y)

point5 = Point(3, 5)
point5.x = 2
print(point5.x, point5.y)
# =========================================
# >>>>> Classes - Inheritance <<<<<


class Mammal:
    def walk(self):
        print('walk')


# Dog extends Mammal class
class Dog(Mammal):
    pass  # pass keyword used when we leave a class empty because class should be empty


# Cat extends Mammal class
class Cat(Mammal):
    def meow(self):
        print('meow.. meow..')


dog = Dog()
dog.walk()

cat = Cat()
cat.walk()
cat.meow()
