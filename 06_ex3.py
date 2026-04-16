#객체지향 클래스
class Person:
    def hello(self):
        print('hello')

    def __init__(self): # 생성자 self 는 this 와 비슷한 개념
        self.hi = 'hello'
    def hello(self):
        print(self.hi)

person = Person()
person.hello()
person1 = Person()
person1.hello()

person2 = Person()
person2.hello()
print(person2)

#속성 정의와 초기화
class Person1:
    def __init__(self, n,a):
        self.name = n
        self.age = a
    def hello(self):
        print('Hello {}'.format(self.name))
        print('당신은 {}살 입니다.'.format(self.age))

person3 = Person1('홍길동', 20)
person3.hello()

#클래스 정의 실습
#학생 클래스(학년, 반, 이름) 생성자 로 설정
# intro 출력 함수
class Student:
    def __init__(self, a, b, c):
        self.grade = a
        self.ban = b
        self.name = c
    def intro(self):
        print('{}학년 {}반 {}입니다.'.format(self.grade , self.ban, self.name))
student1 = Student(2,15, '김연아')
student1.intro()

#비공개 속성 정의
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print('Hello {}'.format(self.name))
        print('당신은 {}살입니다.'.format(self.age))
person4 = Person2('홍길동', 20)
person4.hello()
# print(person.__age) # 에러
# person.__age = 100 # 에러

#비공개 속성 사용
class Person3:
    def __init__(self, name, age):
        self.name = name
        if 0 <= age <=20: self.__age =age
        else: self.__age= 0

    def inc_age(self):
        self.__age += 1
    def info(self):
        print(self.__age)

person5 = Person3('손흥민', 30)
person5.inc_age()
person5.info()

#정적(스태틱) 메서드 사용
class Math:
    @staticmethod
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b

print(Math.add(5,3))
print(Math.sub(2,9))

#클래스 정의 실습
# 사각형을 관리하는 클래스(reduce, )
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    #@staticmethod
    def area(self):
        return self.width * self.height
    def double(self):
        self.width *= 2
        self.height *=2

rect = Rectangle(3,5)
print(rect.area())
rect.double()
print(rect.width, rect.height)

#클래스의 상속
class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def speed_up(self):
        self.speed += 10
    def speed_in(self):
        self.speed -= 10

class Car(Vehicle):
    def __init__(self, speed, wheels, seats):
        Vehicle.__init__(self, speed)
        self.wheels = wheels
        self.seats = seats
    def info(self):
        print(self.speed, self.wheels, self.seats)

car = Car(100,4,4)
car.speed_up()
car.info()

#클래스 상속 실습
class Truck(Car):
    # 생성자
    def __init__(self,speed, wheels, seats, loadage):
        Car.__init__(self, speed, wheels, seats)    #Car의 정의된 생성자 그대로 사용
        self.loadage = loadage
    def load(self):
        print('load')
    def unload(self):
        print('unload')
    #메소드 재정의 Car에 있는 인포를 재정의해서 사용
    def info(self):
        print(self.speed, self.wheels, self.seats, self.loadage)

truck = Truck(100, 6, 2, 30)
truck.load()
truck.unload()
truck.info()