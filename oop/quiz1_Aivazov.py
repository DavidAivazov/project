# დავიდი აივაზოვი - ჯგუფი 3
import sys
import time


class Ticket:
    def __init__(self, film_title, ticket_price, ticket_available, film_language="Geo"):
        self.film_title = film_title
        self.ticket_price = ticket_price
        self.ticket_available = ticket_available
        self.film_language = film_language

    def __str__(self):
        str = (
            f"ფილმის დასახელება: {self.film_title}. ენა: {self.film_language}. ბილეთის ფასი: {self.ticket_price} ₾. ბილეთების მარაგი: {self.ticket_available} ერთეული.")
        return str

    def __gt__(self, other):
        if isinstance(other, Ticket) is True:
            if self.ticket_available > other.ticket_available:
                return True
            else:
                return False
        elif isinstance(other, int) is True:
            if self.ticket_available > other:
                return True

            else:
                return False
        else:
            sys.exit('ფატალური შეცდომა! მიუღებელი შედარება.')

    def __lt__(self, other):
        if isinstance(other, Ticket) is True:
            if self.ticket_available < other.ticket_available:
                return True
            else:
                return False
        elif isinstance(other, int) is True:
            if self.ticket_available < other:
                return True

            else:
                return False
        else:
            sys.exit('ფატალური შეცდომა! მიუღებელი შედარება.')



    def __eq__(self, other):
        if isinstance(other, Ticket) is True:
            if self.ticket_available == other:
                return True
            else:
                return False


        elif isinstance(other, int) is True:
            if self.ticket_available == other:
                return True
            else:
                return False


class User:
    def __init__(self, username, balance):
        self.username = username
        self.balance = balance

    def __str__(self):
        balance = '%.2f' % self.balance
        str = (f"მოგესალმებით, {self.username}! თქვენს ბალანსზე ხელმისაწვდომი თანხა: {balance} ₾. ")
        return str

    def deposit(self):
        deposit = float(input('შეიყვანეთ დეპოზიტის ოდენობა: '))
        while deposit <= 0:
            deposit = float(input('დეპოზიტის ოდენობა უარყოფითი, ან 0 ვერ იქნება! შეიყვანეთ დეპოზიტის ოდენობა: '))
        self.balance += deposit
        print(f'ოპერაცია წარმატებით შესრულებულია! თქვენი მიმდინარე ბალანსი: {self.balance} ₾.')

    def buy_tickets(self, ticket, count):
        if isinstance(ticket, Ticket) is True:
            if (isinstance(count, int) is True) and (count > 0):
                print('მიმდინარეობს მონაცემების დამუშავება...')
                user_balance = self.balance
                tickets_price = ticket.ticket_price * count
                compare_1 = user_balance > tickets_price
                compare_2 = ticket.ticket_available >= count
                time.sleep(2)
                if compare_1 is True:
                    if compare_2 is True:
                        print(
                            'ყველა მონაცემი დამუშავებულია და პირობები დაკმაყოფილებულია! მიმდინარეობს ბილეთის გაფორმება.')
                        self.balance -= tickets_price
                        ticket.ticket_available -= count
                        time.sleep(2)
                        print(
                            f"გილოცავთ! თქვენ შეიძინეთ {count} ბილეთი ფილმზე *{ticket.film_title}*! დარჩენილია {ticket.ticket_available} ბილეთი.")
                    else:
                        print(
                            f'სამწუხაროდ, ბილეთები მოთხოვნილ რაოდენობაში არ არის. ხელმისაწვმდობია {ticket.ticket_available} ბილეთი.')
                else:
                    to_deposit = tickets_price - user_balance
                    print(
                        f'თქვენს ბალანსზე არსებული თანხა({self.balance}) არ არის საკმარისი! გადასახდელი თანხა: {tickets_price} ₾. შეავსეთ ბალანსი {to_deposit} ₾-ით')

            else:
                sys.exit('დაფიქსირდა ფატალური შეცდომა! სცადეთ თავიდან.[1]')
        else:
            sys.exit('დაფიქსირდა ფატალური შეცდომა! სცადეთ თავიდან.[0]')


# test_ticket = Ticket('Titanic', 15, 150)
# print(test_ticket)
# test_user = User('David Aivazov', 1500)
# print(test_user)

def quiz_test():
    Titanic = Ticket('Titanic', 15, 150)
    Prometey = Ticket('Prometey', 14.5, 50, 'Eng')
    Legend = Ticket('I am Legend', 20, 30, )
    print(f"{Titanic}\n{Prometey}\n{Legend})")

    insert_name = str(input('მოგესალმებით! შეიყვანეთ თქვენი სახელი და გვარი: '))
    user1 = User(insert_name, 100)
    print(user1)
    user1.deposit()
    print(user1)
    user1.buy_tickets(Titanic, 5)
    print(user1)
    user1.buy_tickets(Titanic, 150)
    print(user1)
    user1.deposit()
    user1.buy_tickets(Titanic, 145)
    print(user1)
    user1.buy_tickets(Titanic, 5)
    print(user1)
    Titanic2 = Ticket('Titanic2', 25, 150, 'Eng')
    Titanic3 = Ticket('Titanic2', 40, 150)
    print(Titanic2)

    print(f'Titanic2 == Titanic3?: {Titanic2 == Titanic3}')
    print(f'Titanic2 > Titanic3?: {Titanic2 > Titanic3}')
    print(f'Titan2 < Titanic3?: {Titanic2 < Titanic3}')
    print(Titanic)
    print(f'Titanic > Legend?: {Titanic > Legend}')
    print(f'Titanic == Legend?: {Titanic == Legend}')
    print(f'Titanic < Legend?: {Titanic < Legend}')
    print(f'Titanic == 150?: {Titanic == 150}')
    print(f'Titanic == 200?: {Titanic == 200}')
    print(f'Titanic > 140?: {Titanic > 140}')
    print(f'Titanic < 140?: {Titanic < 140}')

# test
quiz_test()
