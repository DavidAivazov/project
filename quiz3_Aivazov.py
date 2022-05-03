# weather api key : 3d54eaad2124ca78ec826c93f2337aa6
# nasa api key: 79YSilSx9Ib8s1sijwvcYvm7vaeAbkXt6jGtzhFQ
# money's coruse: 1f28d79ce4d20eff96bad17a

import json
import sys
import time
from urllib.request import urlretrieve
import sqlite3
from PIL import Image
import requests
from numpy.core.defchararray import capitalize, upper, lower


# getting information about your city's weather and printing it
def weather(city):
    api_key = '3d54eaad2124ca78ec826c93f2337aa6'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    r = requests.get(url)
    result_json = r.text
    res = json.loads(result_json)
    city_name = res['name']
    country_code = res['sys']['country']
    coord_lon = res['coord']['lon']
    coord_lat = res['coord']['lat']
    city_weather = (res['weather'][0]['main'])
    city_sky = capitalize(res['weather'][0]['description'])
    temp = res['main']['temp']
    temp_feel = res['main']['feels_like']
    pressure = res['main']['pressure']
    humidity = res['main']['humidity']
    wind_speed = res['wind']['speed']
    wind_dirrection = res['wind']['deg']
    print(f'ქალაქი: {city_name} [{country_code}] | კოორდინატები: {coord_lon} X {coord_lat} | ამინდი: {city_weather} | '
          f'ღრუბლოვანობა: {city_sky}')
    print(f'ტემპერატურა: {temp} °C (იგრძნება როგორც {temp_feel} °C) | წნევა: {pressure} bar | ტენიანობა: {humidity} %')
    print(f'ქარის სიჩქარე: {wind_speed} მ/წ | ქარის მიმართულება: {wind_dirrection} °')
    time.sleep(1)
    with open('api&parsing/data_weather.json', 'w') as file:
        json.dump(res, file, indent=4)
    print('მონაცემები შეინახა data_weather.json ფაილში!')
    print('მიმდინარეობს გადამისამართება მთავარ მენიუში...')
    time.sleep(1)
    start_program()


# opening image on your computer
def image_open(name):
    im = Image.open(rf"C:\Users\aivaz\OneDrive\Рабочий стол\university\PyFinal\api&parsing\{name}")
    im.show()


def nasa_apod():
    api_key = '79YSilSx9Ib8s1sijwvcYvm7vaeAbkXt6jGtzhFQ'
    count = int(input('რამდენი სურათის ნახვა გსურთ?: '))
    while count <= 0:
        print('სურათების რაოდენობა 0, ან უარყოფითი ვერ იქნება!!!')
        count = int(input('რამდენი სურათის ნახვა გსურთ?: '))
    url = f'https://api.nasa.gov/planetary/apod?count={count}&api_key=79YSilSx9Ib8s1sijwvcYvm7vaeAbkXt6jGtzhFQ'
    r = requests.get(url)
    result_json = r.text
    res = json.loads(result_json)
    res_structured = json.dumps(res, indent=4)
    # print(res_structured)
    pictures = {}
    print('მოიძებნა შემდეგი სურათები: ')
    for i in range(len(res)):
        title = (res)[i]["title"]
        p_url = (res)[i]["url"]
        print(f'{str(title)}: {p_url}')
        pictures[title] = p_url
    time.sleep(1)
    with open('api&parsing/data_apod.json', 'w') as file:
        json.dump(res, file, indent=4)
    print('მონაცემები შეინახა data_apod.json ფაილში!')
    time.sleep(1)
    answer = str(input('გსურთ ამ სურათების გადმოწერა თქვენს კომპიუტერზე?: '))
    show_list = list()
    if answer in ['', 'ki', 'yes', 'კი']:
        for i in range(len(res)):
            title = (res)[i]["title"]
            p_url = (res)[i]["url"]
            print(f'მონაცემები მუშავდება... ინახება: {title}')
            time.sleep(2)
            if ':' in title:
                index = title.index(':')
                title = title[:index]
            elif '/' in title:
                index = title.index('/')
                title = title[:index]
            elif '\\' in title:
                index = title.index('\\')
                title = title[:index]
            elif '*' in title:
                index = title.index('*')
                title = title[:index]
            elif '?' in title:
                index = title.index('?')
                title = title[:index]
            elif '"' in title:
                index = title.index('"')
                title = title[:index]
            elif '<' in title:
                index = title.index('<')
                title = title[:index]
            elif '>' in title:
                index = title.index('>')
                title = title[:index]
            elif '|' in title:
                index = title.index('|')
                title = title[:index]
            if ('youtube' or 'player.vimeo') in p_url:
                # print(f'{p_url} [2]')
                print('მიუღებელი სურათის ფორმატი! სურათი ვერ შეინახა!')

            elif 'jpg' or 'png' or 'gif' in p_url:
                # print(f'{p_url} [1]')
                show_list.append(title)
                urlretrieve(p_url, f"{str(title)}.png")
                print('სურათი წარმატებით შეინახა თქვენს კომპიუტერზე!')
            else:
                # print(f'{p_url} [3]')
                print('მიუღებელი სურათის ფორმატი! სურათი ვერ შეინახა!')
        show_answer = str(input('გსურთ სურათების დათვალიერება?: '))
        if show_answer in ['', 'ki', 'yes', 'კი']:
            print('ხელმისაწვდომია შემდეგი სურათების დათვალიერება: ')
            print(show_list)
            for i in range(len(show_list)):
                print(f'[{i}]: {show_list[i]}')
            show = (input('რომელი სურათის დათვალიერება გსურს?(All = Enter): '))
            if show in ['', 'all', 'ALL', 'All']:
                print('!!!შემდეგი სურათის დათვალიერებისთვის დააჭირეთ ESC(!!!დახურეთ დათვალიერების პროგრამა!!!)')
                time.sleep(2)
                for i in range(len(show_list)):
                    image_open(f'{show_list[i]}.png')
                    time.sleep(1)
            elif int(show) in range(len(show_list)):
                image_open(image_open(f'{show_list[int(show)]}.png'))
            else:
                print('დაფიქსირდა შეცდომა!!! თქვენ აირჩიეთ არავალიდური მოქმედება!!!')
    print('მიმდინარეობს გადამისამართება მთავარ მენიუში...')
    time.sleep(1)
    start_program()
    # nasa_apod()


def money_course():
    api_key = '1f28d79ce4d20eff96bad17a'
    print('თუ გსურთ ვალუტების *კოდის* ინსტრუქცია, შეიყვანეთ HELP')
    money = str(input('რომელი ვალუტის კურსის ნახვა გსურთ?: '))
    while money in ['help', 'Help', 'HELP']:
        print('კოდი იგება შემდეგი მეთოდით, იღება ქვეყნის სიმბოლოები და ემატება ვალუტის დასახელების პირველი ასო')
        print('მაგალითად: GEL (GE - Georgia | L - Lari) USD (US- United States, D-Dollar) ')
        money = str(input('რომელი ვალუტის კურსის ნახვა გსურთ?: '))
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{upper(money)}'
    r = requests.get(url)
    result_json = r.text
    res = json.loads(result_json)
    res_structured = json.dumps(res, indent=4)
    # print(res_structured)
    print('მიმდინარეობს მონაცემების დამუშავება...')
    time.sleep(2)
    status = r.status_code
    print(f'სტატუსი: {status} | სერვერის სტატუსი: {res["result"]}')
    see_headers = str(input('გსურთ ამ request-ის headers-ის დათვალიერება?: '))
    if see_headers in ['კი', 'yes', 'Yes', 'YES', '']:
        print(r.headers)
    if res["result"] == 'success':
        print('მიმდინარეობს მონაცემების დამუშავება...')
        time.sleep(1)
        with open('api&parsing/data_money.json', 'w') as file:
            json.dump(res, file, indent=4)
        print('მონაცემები შეინახა data_money.json ფაილში!')
        time.sleep(1)
        print('ვალუტის დასახელება: ვალუტის ექვივალენტი')
        con_rates = res['conversion_rates']
        for rate in con_rates:
            print(f'{rate} : {con_rates[rate]}')
        add_db = str(input('გსურთ მონაცემების ბაზაში შენახვა?: '))
        if add_db in ['კი', 'yes', '']:
            # setting connection with our DB
            conn = sqlite3.connect(f"{lower(money)}_course.sqlite")
            # adding cursor
            c = conn.cursor()
            # db_name
            db_name = f'{lower(money)}_course'
            # query - creating table with name db_name and values currecncy and value
            c.execute(f'''CREATE TABLE {db_name}
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            currency VARCHAR(50),
            value VARCHAR(100));''')
            # adding values in db
            for rate in con_rates:
                c.execute(f"INSERT INTO {db_name} (currency, value) VALUES (?,?)", (rate, con_rates[rate]))
                conn.commit()
            # getting result
            search_result = c.execute(f"SELECT * FROM {db_name}")
            # printing result
            for row in search_result:
                print(row)
            # close connection
            conn.close()
        continue_ = str(input('გსურთ გაგრძელება?: '))
        if lower(continue_) in ['კი', 'yes', '']:
            money_course()
        else:
            print('მიმდინარეობს გადამისამართება მთავარ მენიუში...')
            time.sleep(2)
            start_program()
    else:
        continue_ = str(input('გსურთ გაგრძელება?: '))
        if lower(continue_) in ['კი', 'yes', '']:
            money_course()
        else:
            print('მიმდინარეობს გადამისამართება მთავარ მენიუში...')
            time.sleep(2)
            start_program()


print('მოგესალმებით, პატივცემულო! ხელმისაწვდომია შემდეგი მოქმედებები: ')
print('P.S. - შეფასებადი არის მე-3 და მე-4 პუნქტები (არასალექციო)')


def start_program():
    print('Сity Weather (1) | NASA APOD (2) | Money Courses (3) | Exit (0)')
    answer = str(input('აირჩიეთ მოქმედება: '))
    if answer == '1':
        city = str(input("შეიყვანეთ თქვენი ქალაქი: "))
        if city == '':
            city = 'Tbilisi'
        weather(city)
    elif answer == '2':
        nasa_apod()
    elif answer == '3':
        money_course()
    elif answer in ['0', 'exit', 'Exit', 'EXIT']:
        sys.exit('Good Bye, dear friend!')
    else:
        print('დაფიქსირდა შეცდომა!!! აირჩიეთ სწორი მოქმედება!!!')
        start_program()


start_program()
