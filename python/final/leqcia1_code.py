import sys
import time

"""
1- შექმენით Rectangle კლასი სურათის მიხედვით. დაამატეთ კლასის კონსტრუქტორი
შესაბამისი ატრიბუტებით. დაამატეთ მართკუხედის ფართობის და პერიმეტრის
გამოსათვლელი ფუნქციები. კლასის გარეთ შემოიღეთ ობიექტები. გამოთვალეთ obj1
ობიექტის ფართობი და დაბეჭდეთ მიღებული შედეგი.
"""


class Rectangle:
    def __init__(self, width, lenght):
        self.width = width
        self.lenght = lenght

    def perimeter(self):
        perimeter = 2 * (self.width + self.lenght)
        return perimeter

    def area(self):
        area = self.width * self.lenght
        return area


def rectangle_check():
    rec_len = float(input("შეიტანეთ მართკუთხედის სიგრძე: "))
    while rec_len <= 0:
        rec_len = float(input("შეიტანეთ მართკუთხედის !დადებითი! სიგრძე: "))
    rec_wid = float(input("შეიყვანეთ მართკუთხედის სიგანე: "))
    while rec_wid <= 0:
        rec_wid = float(input("შეიტანეთ მართკუთხედის !დადებითი! სიგანე: "))
    obj1 = Rectangle(rec_len, rec_wid)
    print(
        f"ჩვენ გვაქვს ოთხკუთხედი, რომლის სიგრძე არის {obj1.lenght}, სიგანე {obj1.width}, მისი პერიმეტრია: {obj1.perimeter()} ერთეული.")
    time.sleep(1)
    print(
        f"ჩვენ გვაქვს ოთხკუთხედი, რომლის სიგრძე არის {obj1.lenght}, სიგანე {obj1.width}, მისი ფართობია: {obj1.area()} კვადრატული ერთეული.")


# test
# rectangle_check()

class Car:

    def __init__(self, model, makeYear, fuelType, color):
        self.model = model
        self.makeYear = makeYear
        self.fuelType = fuelType
        self.color = color

    def buy(self, property):
        print("გამარჯობა! თქვენ შეგიძლიათ იყიდოთ შემდეგი მოდელები: Mercedes, BMW, Audi. Stop - 'stop'")
        stop = 0
        while stop == 0:
            purchare = str(input("რომელი მოდელის ყიდვა გსურთ?: "))
            if purchare == "Mercedes":
                property.append(obj1)
                print(f"გილოცავთ! თქვენ წარმატებულად იყიდეთ {obj1.model}")
            elif purchare == "BMW":
                property.append(obj2)
                print(f"გილოცავთ! თქვენ წარმატებულად იყიდეთ {obj2.model}")
            elif purchare == "Audi":
                property.append(obj3)
                print(f"გილოცავთ! თქვენ წარმატებულად იყიდეთ {obj3.model}")
            elif purchare == "stop":
                stop = 1
            else:
                print("სამწუხაროდ, მითითებული მოდელი არ გვაქვს მარაგში.")

    def sell(self):
        print(f"თქვენ წარმატებულად გაყიდეთ {self.model}!")

    def info(self):
        print(
            f"თქვენი ავტომობილის მწარბოებელი {self.model}, ფერი: {self.color}, ძრავის ტიპი: {self.fuelType}, გამოშვების თარიღი: {self.makeYear}.")

    def rent(self):
        print(f"თქვენ წარმატებულად გააქირავეთ თქვენი მანქანა {self.model}.")

    def insurance(self):
        print(f"თქვენ წარმატებულად დააზღვიეთ თქვენი მანქანა {self.model}.")


obj = Car
obj1 = Car("Mercedes", 2022, "Diesel", "Red")
obj2 = Car("BMW", 2022, "Gas", "Blue")
obj3 = Car("Audi", 2022, "Gas", "Orange")


def test_car():
    property = []
    print(property)
    obj.buy(obj, property)
    obj1.sell()
    obj2.sell()
    obj3.sell()
    obj1.info()
    obj2.info()
    obj3.info()
    obj1.rent()
    obj2.rent()
    obj3.rent()
    obj1.insurance()
    obj2.insurance()
    obj3.insurance()


# test_car()

# print("თქვენ ფლობთ: ")
# for i in (property):
#     print(i.model)
# sell = str(input("რომელი მოდელის გაყიდვა გსურთ?"))
# print(f"თქვენ წარმატებულად გაყიდეთ {property.model}!")
# property.remove(sell)


# test

"""
აღწერეთ კლასი Dog ატრიბუტებით breed, size, age, color. შექმენით 3
ახალი ობიექტი შემდეგი მონაცემების მიხედვით.
"""


class Dog:
    def __init__(self, breed, size, age, color):
        self.breed = breed
        self.size = size
        self.age = age
        self.color = color

    def eat(self):
        print(f"თქვენ აჭამეთ თქვენი {self.breed}.")

    def sleep(self):
        print(f"თქვენი {self.breed}-ს ახლა სძინავს.")

    def sit(self):
        print("აბა! დაჯექი სწრაფად!")
        print(f"თქვენმა {self.breed}-მა დაჯდა ადგილზე.")

    def run(self):
        print("აბა, ვინ მოვიდა?!")
        print(f"თქვენი {self.breed}-ი კარისკენ მირბის. ")

    def specifications(self):
        print(f"თქვენი {self.breed}-ის ზომა არის {self.size}, არის {self.age}, მისი ფერია {self.color}.")


def test_dog():
    obj1 = Dog("Mastif", "Large", "5 y.o.", "Black")
    obj2 = Dog("Maltese", "Small", "2 y.o.", "White")
    obj3 = Dog("Chow Chow", "Medium", "3 y.o.", "Brown")
    obj1.eat()
    obj2.eat()
    obj3.eat()
    obj1.sleep()
    obj2.sleep()
    obj3.sleep()
    obj1.sit()
    obj2.sit()
    obj3.sit()
    obj1.run()
    obj2.run()
    obj3.run()
    obj1.specifications()
    obj2.specifications()
    obj3.specifications()


# test_dog()

class Celsius():
    def __init__(self, temperature):
        self.__temperature = temperature

    def get_temp(self):
        print(f"მიმდინარე ტემპერატურა არის {self.__temperature} გრადუსი.")

    def set_temp(self):
        self.__temperature = float(input("რამდენი გრადუსი არის გარეთ?: "))

    def del_temp(self):
        self.__temperature = 0
        print("თქვენ წაშალეთ ტემპერატურის მაჩვენებელი, დეფოლტად მინიჭებულია 0.")


# test
def test_celsius():
    temp = Celsius(15)
    temp.get_temp()
    temp.set_temp()
    temp.get_temp()
    temp.del_temp()
    temp.get_temp()


# test_celsius()

class Bank_Account:
    def __init__(self, start):
        self.__account_name = ""
        self.__balance = 0.0
        self.start = start
        self.__pin = "0000"

    def pin_getter(self):
        return self.__pin

    def pin_changer(self):
        print("შეიყვანეთ ახალი პინ-კოდი!: ")
        self.__pin = str(input())
        pin = str(input(""))
        while len(str(pin)) != 4:
            print("Pin-კოდის სიგრძე შეადგენს 4 სიმბოლოს! სცადეთ თავიდან!")
            pin = str(input(""))

    def name_setter(self):
        self.__account_name = str(input("ჩაწერეთ თქვენი სახელი და გვარი: "))

    def name_getter(self):
        return self.__account_name

    def balance_setter(self):
        self.__balance = float(input("რა თანხა გაქვთ ანგარიშზე?: "))

    def balance_getter(self):
        return self.__balance

    def balance_correct(self, ammount):
        self.__balance += ammount
        return self.__balance

    def deposit(self):
        ammount = float(input("რა თანხის შეტანა გსურთ?: "))
        while ammount <= 0:
            print("თანხა 0-ზე ნაკლები, ან უარყოფითი ვერ იქნება! სცადეთ თავიდან.")
            ammount = float(input("რა თანხის შეტანა გსურთ?: "))
        self.balance_correct(ammount)

    def withdraw(self):
        ammount = float(input("რა თანხის გატანა გსურთ?: "))
        while ammount <= 0:
            print("თანხა 0-ის ტოლი, ან უარყოფითი ვერ იქნება! სცადეთ თავიდან.")
            ammount = float(input("რა თანხის გატანა გსურთ?: "))
        if ammount > self.balance_getter():
            print(f"თქვენ არ გაქვთ საკმარისი თანხა ანგარიშზე! ხელმისაწვდომი თანხა: {self.balance_getter()}₾")
        else:
            self.balance_correct(-ammount)

    def operations(self, client):
        client.name_setter()
        print(f"მოგესალმებით, პატივცემულო {client.name_getter()}!")
        client.balance_setter()
        print("ხელმისაწვდომია შემდეგი ოპერაციები: ")
        process = 1
        while process == 1:
            print(
                "|1 - თანხის შეტანა| |2 - თანხის გამოტანა| |3 - პინ-კოდის შეცვლა| |4 - ბალანსის ნახვა| |5 - გასვლა|")
            todo = int(input("შეიყვანეთ სასურველი ოპერაციის ნომერი: "))
            if todo == 1:
                client.deposit()
            elif todo == 2:
                client.withdraw()
            elif todo == 3:
                client.pin_changer()
            elif todo == 4:
                print(f"თქვენი ბალანსი არის: {client.balance_getter()}₾")
            elif todo == 5:
                process = 0
        sys.exit("მადლობა, რომ სარგებლობთ ჩვენი მომსახურებით! წარმატებულ დღეს გისურვებთ!")


def test_bank():
    print("Default pin - 0000")
    client = Bank_Account("1")
    print("მიმდინარეობს ბარათის დამუშავება...")
    print("შეიყვანეთ თქვენი Pin-code: ")
    pin = str(input())
    while len(str(pin)) != 4:
        print("Pin-კოდის სიგრძე შეადგენს 4 სიმბოლოს! სცადეთ თავიდან!")
        pin = str(input(""))
    if pin != client.pin_getter():
        try_count = 2
        while try_count > 0:
            print("თქვენ შეიყვანეთ არასწორი პინ-კოდი, სცადეთ თავიდან!")
            pin = str(input(""))
            while len(str(pin)) != 4:
                print("Pin-კოდის სიგრძე შეადგენს 4 სიმბოლოს! სცადეთ თავიდან!")
                pin = str(input(""))
            if pin != client.pin_getter():
                try_count -= 1
            elif pin == client.pin_getter():
                client.operations(client)

        if try_count == 0:
            sys.exit("თქვენ 3-ჯერ შეიყვანეთ არასწორი პინ-კოდი. ბარათი დაბლოკილია!")
    if pin == client.pin_getter():
        client.operations(client)


# test
test_bank()


"""
აღწერეთ კლასი Fraction (წილადი) ატრიბუტებით top და bottom - სადაც top
წარმოადგენს წილადის მრიცხველს, ხოლო bottom წილადის მნიშვნელს. კლასში
დაამატეთ __str__() მეთოდი, რომელიც დააბრუნებს Fraction ტიპის ნებისმიერი
ობიექტს წილადის ფორმატით. მაგ. “3/5”. კლასში დაამატეთ ფუნქცია, რომელიც
დაითვლის ორი წილადის ჯამს და დააბრუნებს შედეგს. ასევე დაამატეთ მეთოდი
inverse(), რომელიც დააბრუნებს წილადის შებრუნებულ მნიშვნელობას. მაგ 3/5-ის
შებრუნებულია 5/3. კლასის გარეთ შემოიტანეთ ორი კონკრეტული ობიექტი
(წილადი) და იპოვეთ მათი ჯამი. დაბეჭდეთ მიღებული შედეგი წილადის
ფორმატით. ასევე დაბეჭდეთ, ერთ-ერთი წილადის შებრუნებული მნიშვნელობა.
"""


class Fraction:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom
    def __str__(self):
        return (f"{self.top}/{self.bottom}")
    def inverce(self):
        return (f"{self.bottom}/{self.top}")
    def sum(self, first, second):
        if first.bottom == second.bottom:
            result = (f"{first.top + second.top}/{first.bottom}")
        else:
            result = (f"{first.top * second.bottom + second.top * first.bottom}/{first.bottom * second.bottom}")
        return result


def test_fraction():
    frac1 = Fraction(3, 7)
    frac2 = Fraction(4, 7)
    frac3 = Fraction(3, 5)
    sum1 = Fraction.sum(Fraction, frac1, frac2)
    sum2 = Fraction.sum(Fraction, frac1, frac3)
    print(sum1)
    print(sum2)
    print(frac1.__str__())
    print(frac1.inverce())


# test
# test_fraction()


"""
აღწერეთ კლასი Point რომლის ატრიბუტებია x და y. შემოიტანეთ Point ტიპის
ობიექტები point1 და point2 რომლის კოორდინატებია (3,5) და (6,9). კლასში დაამატეთ
მეთოდი რომელიც დაითვლის სიგრძეს კოორდინატა ცენტრიდან ნებისმიერ
წერტილამდე.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 6
    def distance_from_center(self):
        distance = (self.x ** 2 + self.y ** 2) ** 0.5
        return distance

    # 7
    def __str__(self):
        return (f"({self.x},{self.y})")

    # ( (x2-x1)2 + (y2-y1)2 ) 1/2
    def distance_from_points(self, first, second):
        distance = ((second.x - first.x) ** 2 + (second.y - first.y) ** 2) ** 0.5
        return distance


def test_point():
    # 6
    point1 = Point(3, 5)
    point1_d = point1.distance_from_center()
    point2 = Point(6, 9)
    point2_d = point2.distance_from_center()
    print(f"წერტილი: ({point1.x},{point1.y}). მანძილი ცენტრიდან: {point1_d}")
    print(f"წერტილი: ({point2.x},{point2.y}). მანძილი ცენტრიდან: {point2_d}")
    # 7
    print(point1.__str__())
    x1 = int(input("შეიყვანეთ а წერტილის Х: "))
    y1 = int(input("შეიყვანეთ а წერტილის Y: "))
    a = Point(x1, y1)
    print(f"a: {a.__str__()}")
    x2 = int(input("შეიყვანეთ b წერტილის Х: "))
    y2 = int(input("შეიყვანეთ b წერტილის Y: "))
    b = Point(x2, y2)
    print(f"b: {b.__str__()}")
    distance = Point.distance_from_points(Point, a, b)
    print(f"მანძილი а:{a.__str__()} და b:{b.__str__()} შორის არის: {distance}")


# test
test_point()
