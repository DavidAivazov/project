import sys


class Cat:
    def eat(self):
        print('Cat eats a milk :) ')

    def talk(self):
        print('Cat says meowwww')

    def walk(self):
        print('Cat can run 20 km/h')


class Dog:
    def eat(self):
        print('Dog eats a bone :) ')

    def talk(self):
        print('Dog says awwww!')

    def walk(self):
        print('Dog can run 40 km/h')


# 1
def animals_test():
    cat1 = Cat()
    dog1 = Dog()
    n_tuple = (cat1, dog1)
    for i in n_tuple:
        i.talk()
        i.walk()
        i.eat()


# animals_test()


class Currency:
    def __init__(self, value, unit="GEL"):
        self.value = value
        self.unit = unit

    def __str__(self):

        money_value = '%.2f' % self.value
        return_value = (f"{(money_value)} {self.unit}")
        return return_value

    def changeTo(self, convertTo):
        # 1USD = 0.90EUR
        # 1USD = 3.21GEL
        # 1EUR = 1.11USD
        # 1EUR = 3.56GEL
        # 1GEl = 0.28EUR
        # 1GEl = 0.31USD

        if self.unit == "USD" and convertTo == "EUR":
            self.value *= 0.9
            self.unit = "EUR"
        elif self.unit == "USD" and convertTo == "GEL":
            self.value *= 3.21
            self.unit = "GEL"
        elif self.unit == "EUR" and convertTo == "USD":
            self.value *= 1.1
            self.unit = "USD"
        elif self.unit == "EUR" and convertTo == "GEL":
            self.value *= 3.56
            self.unit = "GEL"
        elif self.unit == "GEL" and convertTo == "EUR":
            self.value *= 0.28
            self.unit = "EUR"
        elif self.unit == "GEL" and convertTo == "USD":
            self.value *= 0.31
            self.unit = "USD"
        elif self.unit == convertTo:
            pass

    def __add__(self, other):
        if isinstance(other, Currency) is False:
            self.value += other
        elif isinstance(other, Currency) is True:
            other.changeTo(self.unit)
            self.value += other.value
        return self

    def __radd__(self, other):
        if isinstance(other, Currency) is False:
            self.value += other
        elif isinstance(other, Currency) is True:
            other.changeTo(self.unit)
            self.value += other.value
        return self

    def __mul__(self, other):
        if (isinstance(other, int) or isinstance(other, float)) is True:
            self.value *= other
            return self
        else:
            print('გამრავლების ოპერაცია უნდა შესრულდეს მხოლოდ მთელ ანათწილად რიცხვზე')

    def __rmul__(self, other):
        if (isinstance(other, int) or isinstance(other, float)) is True:
            self.value *= other
            return self
        else:
            print('გამრავლების ოპერაცია უნდა შესრულდეს მხოლოდ მთელ ანათწილად რიცხვზე')

    def __lt__(self, other):
        if (isinstance(self, Currency) and isinstance(other, Currency)) is True and self.unit == other.unit:
            if self.value < other.value:
                return True
            else:
                return False
        elif (isinstance(self, Currency) and isinstance(other, Currency)) is True and self.unit != other.unit:
            other.changeTo(self.unit)
            if self.value < other.value:
                return True
            else:
                return False
        else:
            print('შედარების ოპერაცია უნდა შესრულდეს მხოლოდ Сurrent კლასის შვილებს შორის')

    def __gt__(self, other):
        if (isinstance(self, Currency) and isinstance(other, Currency)) is True and self.unit == other.unit:
            if self.value > other.value:
                return True
            else:
                return False
        elif (isinstance(self, Currency) and isinstance(other, Currency)) is True and self.unit != other.unit:
            other.changeTo(self.unit)
            if self.value > other.value:
                return True
            else:
                return False
        else:
            print('შედარების ოპერაცია უნდა შესრულდეს მხოლოდ Сurrent კლასის შვილებს შორის')


# test
def test_currency():
    test1 = Currency(100, "EUR")
    test2 = Currency(100, "USD")
    test3 = Currency(100)

    print(test1 > test2)
    print(test1 < test2)
    print(test1 > 15)


# test_currency()


class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        init = (f'მოგესალმებით, {self.name}! თქვენს დეპოზიტზე არსებული თანხა: {self.deposit} ₾. აღებული სეხსი: {self.loan} ₾.')
        return init

class House:
    def __init__(self, ID, price, owner, status='გასაყიდი'):
        self.id = ID
        self.price = price
        self.owner = owner
        self.status = status

    def sell_house(self, buyer, loan = 0):
        if loan < 0:
            sys.exit('დაფიქსირდა შეცდომა! სესხის ოდენობა უარყოფითი ვერ იქნება!')
        seller = self.owner
        print(f'მიმდინარეობს ბინის [{self.id}] გაყიდვის პროცესი.')
        seller.deposit += self.price
        self.owner = buyer.name
        buyer.loan += loan
        if loan == 0:
            self.status = 'გაყიდული'
        else: self.status = 'გაყიდულია სესხით'
        print(f'{seller.name}-მა გაყიდა ბინა [{self.id}], ახალი მფლობელი- {buyer.name}! ბინის ღირებულება: {self.price} ₾')

def per_house():
    per1 = Person('David Aivazov', 3500)
    per2 = Person('Franklin Houston')
    flat1 = House('0001', 150000, per1)
    flat2 = House('0002', 145000, per2)
    print(per1)
    print(per2)
    print(flat1.owner)
    print(flat1.status)
    print(flat1.sell_house(per2))
    print(flat1.status)
    print(flat2.owner)
    print(flat2.status)
    print(flat2.sell_house(per1, 140000))
    print(flat2.status)
    print(per1)
    print(per2)

# per_house()