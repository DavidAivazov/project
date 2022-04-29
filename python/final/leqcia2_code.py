class Shape:
    def __init__(self, color):
        self.color = color

    def say_hi(self):
        print(f"I am a shape with {self.color} color :)")


class Quadrangle(Shape):
    def __init__(self, a, b, c, d, color):
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def say_hi(self):
        super().say_hi()
        print(f"Hi! I am a Quadrangle with color {self.color} and sides: {self.a, self.b, self.c, self.d}")


#
# s1 = Shape("red")
# s1.say_hi()
# q1 = Quadrangle(3, 6, 8, 1, "Blue")
# q1.say_hi()


class People:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_email(self, status):
        if status == 1:
            mail = (f"{self.firstname.lower()}.{self.lastname.lower()}.uni@btu.edu.ge")
            return mail
        elif status == 2:
            mail = (f"{self.firstname.lower()}.{self.lastname.lower()}@btu.edu.ge")
            return mail
        elif status == 3:
            mail = (f"{self.firstname.lower()}.{self.lastname.lower()}.1@btu.edu.ge")
            return mail


class Lecturer(People):
    def __init__(self, firstname, lastname, salary):
        self.salary = salary
        super().__init__(firstname, lastname)


class Student(People):
    def __init__(self, firstname, lastname, courses):
        self.courses = courses
        super().__init__(firstname, lastname)


class Doctoral_student(Lecturer, Student):
    def __init__(self, firstname, lastname, salary, courses):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.courses = courses


def people_test():
    obj1 = People("David1", "Aivazov")
    obj2 = Lecturer("David2", "Aivazov", "$1500")
    obj3 = Student("David3", "Aivazov", ["Python"])
    obj4 = Doctoral_student("Student", "Doctor", "$500", ["Python", "C#", "C++"])
    print(obj1.get_email(1))
    print(obj2.get_email(2))
    print(obj2.salary)
    print(obj3.get_email(3))
    print(obj3.courses)
    print(obj4.get_email(3))
    print(obj4.courses)
    print(obj4.salary)


# test
people_test()


class Libraryitem:
    def __init__(self, title, subject, status):
        self.title = title
        self.subject = subject
        self.status = status

    def booking(self):
        if self.status == "occupied":
            print(f"სამწუხაროდ, {self.title} ამჟამად არ არის ხელმისაწვდომი.")
        elif self.status == "available":
            print(f"თქვენ წარმატებულად დაჯავშნეთ {self.title}!")
            self.status = "occupied"
        else:
            print(f"დაფიქსირდა შეცდომა, სცადეთ მოგვიანებით!")


class Book(Libraryitem):
    def __init__(self, ISBN, authors, title, subject, status):
        self.ISBN = ISBN
        self.authors = authors
        super().__init__(title, subject, status)


class Magazine(Libraryitem):
    def __init__(self, journalName, volume, status):
        self.title = journalName
        self.volume = volume
        self.status = status


class CD(Libraryitem):
    def __init__(self, title, status):
        super().__init__(title, None, status)

    def booking(self):
        print(f"სამწუხაროდ, ბიბლიოთეკაში CD-ის დაჯავშნა არ არის შესაძლებელი!")


def library_test():
    obj1 = Libraryitem("Testbook", "Testing code", "available")
    obj2 = Libraryitem("Testbook2", "Testing code, but in other variable", "occupied")
    obj1.booking()
    obj1.booking()
    obj2.booking()
    obj3 = Book("552335", "David Aivazov", "Breaking brains", "Just for testing code", "available")
    obj4 = Book("55233552", "David Aivazov", "Breaking brains2", "Just for testing code2", "occupied")
    obj3.booking()
    obj3.booking()
    obj4.booking()
    obj5 = Magazine("The Times", "2022", "available")
    obj6 = Magazine("New York Times", "2021", "occupied")
    obj5.booking()
    obj5.booking()
    obj6.booking()
    a = CD("title", "available")
    a.booking()


# test
# library_test()


class Contacts:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class MailSender:
    def send_mail(self):
        print("თქვენი მეილი გაიგზავნა ამ მისამართზე: giorgi.giorgadze@gmail.com")


class Friend(Contacts, MailSender):
    def __init__(self, name, phone, email):
        super().__init__(name, phone)
        self.email = email


class Family(Contacts, MailSender):
    def __init__(self, name, email, phone, birthdate):
        super().__init__(name, phone)
        self.email = email
        self.birthdate = str(birthdate)


def test_contacts():
    obj1 = Friend("David", "123", "mail.ru")
    obj1.send_mail()
    obj2 = Family("David", "mail2.ru", "321", "bubu22")
    obj2.send_mail()

# test
# test_contacts()
