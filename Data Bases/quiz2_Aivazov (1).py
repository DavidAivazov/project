import sys
import sqlite3
import time
import matplotlib.pyplot as plt


# importing necessary libraries

# this function is setting connection with oscar database
def oscar_db_con():
    conn = sqlite3.connect('oscar_winners.sqlite')
    return conn


# this function is redirecting code to main menu from sortlist menu
def oscar_finish_sortlist():
    print('ოპერაცია დასრულებულია! მიმდინარეობს გადამისამართება წინა მენიუში...')
    time.sleep(2)
    oscar_sort_list()


# this function is redirecting code to main menu from add people menu
def oscar_finish_addp():
    print('ოპერაცია დასრულებულია! მიმდინარეობს გადამისამართება წინა მენიუში...')
    time.sleep(2)
    oscar_db_todo()


# this function is redirecting code to main menu from update menu
def oscar_finish_upd():
    print('ოპერაცია დასრულებულია! მიმდინარეობს გადამისამართება წინა მენიუში...')
    time.sleep(2)
    oscar_db_todo()


# this function is redirecting code to main menu from delete menu
def oscar_finish_del():
    print('ოპერაცია დასრულებულია! მიმდინარეობს გადამისამართება წინა მენიუში...')
    time.sleep(2)
    oscar_db_todo()


# this function is redirecting code to count menu from count(inside) menu
def oscar_finish_incount():
    print('მიმდინარეობს წინა მენიუში გადასვლა...')
    time.sleep(2)
    oscar_count_list()


# this function is redirecting code to main menu from countlist menu
def oscar_finish_count():
    print('ოპერაცია დასრულებულია! მიმდინარეობს გადამისამართება წინა მენიუში...')
    time.sleep(2)
    oscar_db_todo()


# this function is redirecting code to main menu from diagramme menu
def oscar_finish_diagramme():
    print('ოპერაცია დასრულებულია! მიმდინარეობს გადამისამართება წინა მენიუში...')
    time.sleep(2)
    oscar_diagramme_list()


# this function is sorting data with year(input) and, if you want, it can print results
# input year int type, db query, results'count and result(c.execute), which is pushing query with year in
# db and getting values with fetchone/many/all function
def oscar_sortby_year(c=oscar_db_con().cursor()):
    year = int(input('რომელი წლის ოსკარების გამოტანა ხსურთ?: '))
    while year <= 1927:
        print('ოსკარები 1927 წლამდე არ არსებობს! სცადეთ სხვა თარიღი! ( 1928+ )')
        year = int(input('რომელი წლის ოსკარების გამოტანა ხსურთ?: '))
    query = "Select * from oscar where year=?"
    how_much = (input('რამდენი ჩანაწერის გამოტანა გსურთ? (ყველა-All) : '))
    while how_much is int and how_much < 0:
        print('ჩანაწერის რაოდენობა 0, ან უარყოფითი ვერ იქნება! სცადეთ თავიდან')
        how_much = (input('რამდენი ჩანაწერის გამოტანა გსურთ? (ყველა-All) : '))
    c.execute(query, (year,))
    print('(id, year, age, name, gender, movie)')
    if how_much == '1':
        records = c.fetchone()
        print(records)
    elif how_much in ['All', 'all', 'ALL', '']:
        records = c.fetchall()
        for record in records:
            print(record)
    else:
        # add count and compare code for solve errors
        records = c.fetchmany(int(how_much))
        for record in records:
            print(record)
    oscar_finish_sortlist()


# this function is sorting data with age(input) and, if you want, it can print results
# input age int type, db query, results'count and result(c.execute), which is pushing query with age in
# db and getting values with fetchone/many/all function
def oscar_sortby_age(c=oscar_db_con().cursor()):
    age = int(input('რა ასაკის ოსკარების მფლობლების გამოტანა ხსურთ?: '))
    while age <= 0:
        print('ასაკი 0, ან უარყოფითი ვე იქნება! სცადეთ თავიდან!')
        age = int(input('რა ასაკის ოსკარების მფლობლების გამოტანა ხსურთ?: '))
    query = "Select * from oscar where age=?"
    how_much = (input('რამდენი ჩანაწერის გამოტანა გსურთ? (ყველა-All) : '))
    while how_much is int and how_much < 0:
        print('ჩანაწერის რაოდენობა 0, ან უარყოფითი ვერ იქნება! სცადეთ თავიდან')
        how_much = (input('რამდენი ჩანაწერის გამოტანა გსურთ? (ყველა-All) : '))
    c.execute(query, (age,))
    print('(id, year, age, name, gender, movie)')
    if how_much == '1':
        records = c.fetchone()
        print(records)
    elif how_much in ['All', 'all', 'ALL', '']:
        records = c.fetchall()
        for record in records:
            print(record)
    else:
        # add count and compare code for solve errors
        records = c.fetchmany(int(how_much))
        for record in records:
            print(record)
    oscar_finish_sortlist()


# this function is sorting data with sex(input) and, if you want, it can print results
# 1- input sex str type, db query, results'count and result(c.execute), which is pushing query with sex in
# db and getting values with fetchone/many/all function
def oscar_sortby_sex(c=oscar_db_con().cursor()):
    sex = str(input('რა სქესის ოსკარების მფლობლების გამოტანა ხსურთ?: '))
    if sex in ['F', 'f', 'FEMALE', 'female', 'Female']:
        sex = 'F'
    elif sex in ['M', 'm', 'MALE', 'male', 'Male']:
        sex = 'M'
    else:
        print('სულ ხელმისაწვდომია 2 გენდერი! Male/Female!')
        oscar_sortby_sex()
    query = "Select * from oscar where gender=?"
    how_much = (input('რამდენი ჩანაწერის გამოტანა გსურთ? (ყველა-All) : '))
    while how_much is int and how_much < 0:
        print('ჩანაწერის რაოდენობა 0, ან უარყოფითი ვერ იქნება! სცადეთ თავიდან')
        how_much = (input('რამდენი ჩანაწერის გამოტანა გსურთ? (ყველა-All) : '))
    c.execute(query, (sex,))
    print('(id, year, age, name, gender, movie)')
    if how_much == '1':
        records = c.fetchone()
        print(records)
    elif how_much in ['All', 'all', 'ALL', '']:
        records = c.fetchall()
        for record in records:
            print(record)
    else:
        # add count and compare code for solve errors
        records = c.fetchmany(int(how_much))
        for record in records:
            print(record)
    oscar_finish_sortlist()


# this function is sorting data with name(input) and, if you want, it can print results
# 1- input name str type, db query, results'count and result(c.execute), which is pushing query with name in
# db and getting values with fetchone/many/all function
def oscar_sortby_name(c=oscar_db_con().cursor()):
    name = str(input('შეიტანეთ ოსკარის მფლობლის სახელი: '))
    query = "Select * from oscar where name=?"
    how_much = (input('რამდენი ჩანაწერის გამოტანა გსურთ? (ყველა-All) : '))
    while how_much is int and how_much < 0:
        print('ჩანაწერის რაოდენობა 0, ან უარყოფითი ვერ იქნება! სცადეთ თავიდან')
        how_much = (input('რამდენი ჩანაწერის გამოტანა გსურთ? (ყველა-All) : '))
    c.execute(query, (name,))
    print('(id, year, age, name, gender, movie)')
    if how_much == '1':
        records = c.fetchone()
        if records is None:
            print('ასეთი სახელით ოსკარის მფლობელი ვერ მოიძებნა!')
            oscar_finish_sortlist()
        print(records)
    elif how_much in ['All', 'all', 'ALL', '']:
        records = c.fetchall()
        for record in records:
            print(record)
    else:
        # add count and compare code for solve errors
        records = c.fetchmany(int(how_much))
        for record in records:
            print(record)
    oscar_finish_sortlist()


# this function is sorting data with id(input) and, if you want, it can print results
# 1- input id int type, db query, results'count and result(c.execute), which is pushing query with id in
# db and getting values with fetchone/many/all function
def oscar_sortby_id(c=oscar_db_con().cursor()):
    id = str(input('შეიტანეთ ოსკარის ID: '))
    query = "Select * from oscar where id=?"
    c.execute(query, (id,))
    print('(id, year, age, name, gender, movie)')
    records = c.fetchall()
    for record in records:
        print(record)
    oscar_finish_sortlist()


# this function is sorting data with title(input) and, if you want, it can print results
# 1- input title str type, db query, results'count and result(c.execute), which is pushing query with title in
# db and getting values with fetchone/many/all function
def oscar_sortby_title(c=oscar_db_con().cursor()):
    title = str(input('შეიტანეთ ოსკარის Title: '))
    query = "Select * from oscar where movie=?"
    c.execute(query, (title,))
    print('(id, year, age, name, gender, movie)')
    records = c.fetchall()
    for record in records:
        print(record)
    oscar_finish_sortlist()


# this is sort-menu function, where you can choose action with input(choice), if choice = n -> then will work
# function with number n, Exit function is closing connection with database, which was opened in oscar_db,
# which was called in main menu(choice db)
def oscar_sort_list(c=oscar_db_con()):
    print('თქვენ აირჩიეთ მონაცემების მოძებნა/სორტირება! რის მიხედვით გსურთ სორტირება?')
    print('წელი(1) | ასაკი(2) | სქესი(3) | სახელი(4) | ID (5) | ფილმი(6) | მენიუში დაბრუნება (7) | EXIT(0)')
    choice = str(input('შეიყვანეთ სასურველი მოქმედება: '))
    if choice == '1':
        oscar_sortby_year()
    elif choice == '2':
        oscar_sortby_age()
    elif choice == '3':
        oscar_sortby_sex()
    elif choice == '4':
        oscar_sortby_name()
    elif choice == '5':
        oscar_sortby_id()
    elif choice == '6':
        oscar_sortby_title()
    elif choice == '7':
        print('მიმდინაორებს მენიუში გადასვლა...')
        time.sleep(2)
        oscar_db_todo()
    elif choice == '0':
        print('მიმდინარეობს პროცესების შეწყვეტა...')
        time.sleep(1)
        c.close()
        sys.exit('Goodbye, dear friend!')


# with this function  you can add data in oscar_db, max_id is maximum id in the db, you can't add id, which
# equals, or less, than this max_id, while code == 1 you cann add data in db with inputs, then
# when you will fill all vars, they will be sent in add_q query, which will push with c.execute, then
# program will commit this data in database with conn.commit function, if user will want to continue code,
# he will answer 1 in answer input(str) var, then while cycle will repeat untill user will write something
# except 1 for leaving while cycle
def oscar_add_person(conn=oscar_db_con()):
    c = conn.cursor()
    max_id_r = c.execute('Select max(id) from oscar')
    max_id = c.fetchone()
    # print(max_id[0])
    code = 1
    while code == 1:
        print('თქვენ აირჩიეთ ახალი მონაცემის დამატება! მიყევით ქვევით მოყვანილ ინსტრუქციებს!')
        print('მონაცემები ინახება შემდეგი სახით: (id, year, age, name, gender, movie)')
        print('თუ გსურთ მენიუში დაბრუნება, შეიყვანეთ "Menu"')
        p_id = max_id[0] + 1
        print('P.S. - მენიუში დაბრუნება შემდეგ პუნქტზე ვერ იმუშავებს!!!')
        year = int(input('შეიყვანეთ ოსკარის გაცემის წელიწადი: '))
        while year <= 1927:
            print('ოსკარები 1927 წლამდე არ არსებობს! სცადეთ სხვა თარიღი! ( 1928+ )')
            year = int(input('შეიყვანეთ ოსკარის გაცემის წელიწადი: '))
        print('P.S. - მენიუში დაბრუნება შემდეგ პუნქტზე ვერ იმუშავებს!!!')
        age = int(input('შეიყვანეთ ოსკარის მიმღების ასაკი: '))
        while age <= 0:
            print('ასაკი 0, ან უარყოფითი ვერ იქნება! შეიყვანეთ რეალური ასაკი')
            age = int(input('შეიყვანეთ ოსკარის მიმღების ასაკი: '))
        name = str(input('შეიყვანეთ ოსკარის მიმღების სახელი და გვარი: '))
        if name == 'Menu':
            oscar_finish_addp()
        sex = str(input('შეიყვანეთ ოსკარის მიმღების სქესი (Male/Female (M/F)): '))
        if sex in ['Male', 'MALE', 'male', 'M']:
            sex = 'M'
        elif sex in ['Female', 'FEMALE', 'female', 'F']:
            sex = 'F'
        elif sex == 'Menu':
            oscar_finish_addp()
        else:
            sex = '?'
        movie = str(input('შეიყვანეთ ფილმის დასახელება: '))
        if movie == 'Menu':
            oscar_finish_addp()
        add_q = 'Insert into oscar (id, year, age, name, gender, movie) values (?, ?, ?, ?, ?, ?)'
        c.execute(add_q, (p_id, year, age, name, sex, movie))
        print('მონაცემები მუშავდება...')
        time.sleep(2)
        conn.commit()
        answer = str(input('მონაცემები წარმატებულად დამატდა! გსურთ გაგრძელება?(კი/არა): '))
        if answer in ['არა', '0']:
            code = 0
        else:
            code = 1
    oscar_finish_addp()


# with this function  you can update data in oscar_db, max_id is maximum id in the db, you can't update data, which id
# equals, or less, than this max_id, while code == 1 you cann add data in db with inputs, then
# when you will fill all vars, they will be sent in u_query, which will push with c.execute, then
# program will commit this data in database with conn.commit function, then program will search updated data
# with u_query, will find it with c.execute function and will caught this result with fetchone function
# and will print it in console, if user will want to continue code,
# he will answer 1 in answer input(str) var, then while cycle will repeat untill user will write something
# except 1 for leaving while cycle
def oscar_update_p(conn=oscar_db_con()):
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    max_id_r = c.execute('Select max(id) from oscar')
    max_id = c.fetchone()
    code = 1
    while code == 1:
        print('თქვენ აირჩიეთ ახალი მონაცემის შეცვლა/განახლება! მიყევით ქვევით მოყვანილ ინსტრუქციებს!')
        print('მონაცემები ინახება შემდეგი სახით: (id, year, age, name, gender, movie)')
        p_id = int(input("რომელი ID'ს მქონე ჩანაწერის შეცვლა გსურთ?: "))
        while p_id > max_id[0]:
            print(f"შეყვანილი ID ვერ მოიძებნება! მაქსიმალური ხელმისაწვდომი ID: {max_id[0]}")
            p_id = int(input("რომელი ID'ს მქონე ჩანაწერის შეცვლა გსურთ?: "))
        print('მონაცემები მუშავდება...')
        time.sleep(2)
        s_query = "Select * from oscar where id=?"
        c.execute(s_query, (p_id,))
        records = c.fetchone()
        print('თქვენ გსურთ შემდეგი ჩანაწერის შეცვლა: ')
        print(tuple(records))
        print("P.S. - თუ არ გსურთ მონაცემის შეცვლა, დატოვეთ ველი ცარიელად და დააწკაპეთ ENTER'ს ")
        print('თუ გსურთ მენიუში დაბრუნება, შეიყვანეთ "Menu"')
        id = (input('შეიყვანეთ ოსკარის ID: '))
        if id == '':
            id = records['id']
        elif id == 'Menu':
            oscar_finish_upd()
        year = (input('შეიყვანეთ ოსკარის გაცემის წელიწადი: '))
        if year == '':
            year = records['year']
        elif year == 'Menu':
            oscar_finish_upd()
        while year <= 1927:
            print('ოსკარები 1927 წლამდე არ არსებობს! სცადეთ სხვა თარიღი! ( 1928+ )')
            year = int(input('შეიყვანეთ ოსკარის გაცემის წელიწადი: '))
            if year == '':
                year = records['year']
        age = (input('შეიყვანეთ ოსკარის მიმღების ასაკი: '))
        if age == '':
            age = records['age']
        elif age == 'Menu':
            oscar_finish_upd()
        name = (input('შეიყვანეთ ოსკარის მიმღების სახელი და გვარი: '))
        if name == '':
            name = records['name']
        elif name == 'Menu':
            oscar_finish_upd()
        sex = str(input('შეიყვანეთ ოსკარის მიმღების სქესი (Male/Female (M/F)): '))
        if sex == '':
            sex = records['gender']
        elif sex in ['Male', 'MALE', 'male', 'M']:
            sex = 'M'
        elif sex in ['Female', 'FEMALE', 'female', 'F']:
            sex = 'F'
        elif sex == 'Menu':
            oscar_finish_upd()
        else:
            sex = '?'
        movie = str(input('შეიყვანეთ ფილმის დასახელება: '))
        if movie == '':
            movie = records['movie']
        elif movie == 'Menu':
            oscar_finish_upd()
        u_query = 'Update oscar set id = ?, year = ?, age = ?, name = ?, gender = ?, movie = ? where id = ?'
        c.execute(u_query, (p_id, year, age, name, sex, movie, p_id))
        conn.commit()
        print('მონაცემები მუშავდება...')
        time.sleep(2)
        print('წარმატებით შეიცვალა! იხილეთ შეცვლილი მონაცემი: ')
        s_query = "Select * from oscar where id=?"
        c.execute(s_query, (p_id,))
        records = c.fetchone()
        print(tuple(records))
        answer = str(input('მონაცემები წარმატებულად დამატდა! გსურთ გაგრძელება?(კი/არა): '))
        if answer in ['არა', '0']:
            code = 0
        else:
            code = 1
    oscar_finish_upd()


# with this function  you can delete data from oscar_db, max_id is maximum id in the db, you can't delete data, which id
# equals, or less, than this max_id, while code == 1 you cann delete data in db with inputs, then
# when you will fill all vars, they will be sent in s_query, which will push with c.execute, then
# program will ask you if you are sure, or not and if you will answer yes, it will delete this data from
# database with conn.commit function, then program will search updated data
# with u_query, will find it with c.execute function and will caught this result with fetchone function
# and will print it in console, if user will want to continue code,
# he will answer 1 in answer input(str) var, then while cycle will repeat untill user will write something
# except 1 for leaving while cycle
def oscar_delete_p(conn=oscar_db_con()):
    c = conn.cursor()
    max_id_r = c.execute('Select max(id) from oscar')
    max_id = c.fetchone()
    code = 1
    while code == 1:
        print('თქვენ აირჩიეთ ახალი მონაცემის წაშლა! მიყევით ქვევით მოყვანილ ინსტრუქციებს!')
        print('მონაცემები ინახება შემდეგი სახით: (id, year, age, name, gender, movie)')
        p_id = int(input("რომელი ID'ს მქონე ჩანაწერის წაშლა გსურთ?: "))
        while p_id > max_id[0]:
            print(f"შეყვანილი ID ვერ მოიძებნება! მაქსიმალური ხელმისაწვდომი ID: {max_id[0]}")
            p_id = int(input("რომელი ID'ს მქონე ჩანაწერის შეცვლა გსურთ?: "))
        print('მონაცემები მუშავდება...')
        time.sleep(2)
        s_query = "Select * from oscar where id=?"
        c.execute(s_query, (p_id,))
        records = c.fetchone()
        print('თქვენ გსურთ შემდეგი ჩანაწერის წაშლა: ')
        print(records)
        sure = input('თქვენ ნამდვილად გსურთ მონაცემის წაშლა?(კი/არა): ')
        if sure in ['კი', '1', 'yes', '']:
            print('მონაცემები მუშავდება...')
            time.sleep(2)
            d_query = f'Delete from oscar where id ={p_id}'
            c.execute(d_query)
            conn.commit()
            answer = str(input('მონაცემი წარმატებით წაიშალა! გსურთ გაგრძელება?: '))
            if answer in ['არა', '0']:
                code = 0
            else:
                code = 1
        else:
            answer = str(input('ოპერაცია დასრულებულია, გსურთ გაგრძელება?: '))
            if answer in ['არა', '0']:
                code = 0
            else:
                code = 1
    oscar_finish_del()


# with this function  you can count data in oscar_db with year, for that you need to input year,
# then your answer will be sent in query, which will push with c.execute function. result
# will save in found var with fetchone function, and we will get only value with [0] index of
# values list from fetchone, program will ask you if you want to view the result, if answer will yes, then
# program will find this data with query and execute functions, and will print it. if user will want to continue code,
# he will answer 1 in answer input(str) var, then while cycle will repeat untill user will write something
# except 1 for leaving while cycle
def oscar_count_year(conn=oscar_db_con()):
    code = 1
    c = conn.cursor()
    print('თქვენ აირჩიეთ მონაცემის დათვლა წლის მიხედვით! მიყევით ინსტრუქციებს!')
    while code == 1:
        year = int(input('რომელი წლის ოსკარების დათვლა გსურთ?: '))
        while year <= 1927:
            print('ოსკარები 1927 წლამდე არ არსებობს! სცადეთ სხვა თარიღი! ( 1928+ )')
            year = int(input('რომელი წლის ოსკარების გამოტანა ხსურთ?: '))
        query = ('Select count(*) from oscar where year =?')
        c.execute(query, (year,))
        found = c.fetchone()[0]
        print(f'მოიძებნა {found} მონაცემი.')
        if found != 0:
            answer = str(input('გსურთ მონაცემების დათვალიერება?: '))
            if answer in ['კი', '']:
                query = ('Select * from oscar where year =?')
                c.execute(query, (year,))
                records = c.fetchall()
                print('მონაცემები ინახება შემდეგი სახით: (id, year, age, name, gender, movie)')
                for record in records:
                    print(record)
        continue_ans = str(input('გსურთ გაგრძელება?: '))
        if continue_ans in ['კი', '']:
            code = 1
        else:
            code = 0
    oscar_finish_incount()


# with this function  you can count data in oscar_db with age, for that you need to input age,
# then your answer will be sent in query, which will push with c.execute function. result
# will save in found var with fetchone function, and we will get only value with [0] index of
# values list from fetchone, program will ask you if you want to view the result, if answer will yes, then
# program will find this data with query and execute functions, and will print it. if user will want to continue code,
# he will answer 1 in answer input(str) var, then while cycle will repeat untill user will write something
# except 1 for leaving while cycle
def oscar_count_age(conn=oscar_db_con()):
    code = 1
    c = conn.cursor()
    print('თქვენ აირჩიეთ მონაცემის დათვლა ასაკის მიხედვით! მიყევით ინსტრუქციებს!')
    while code == 1:
        age = int(input('რა ასაკის ოსკარების მფლობლების დათვლა გსურთ?: '))
        while age <= 0:
            print('ასაკი 0, ან უარყოფითი ვერ იქნება! სცადეთ თავიდან!')
            age = int(input('რა ასაკის ოსკარების მფლობლების დათვლა გსურთ?: '))
        query = ('Select count(*) from oscar where age =?')
        c.execute(query, (age,))
        found = c.fetchone()[0]
        print(f'მოიძებნა {found} მონაცემი.')
        if found != 0:
            answer = str(input('გსურთ მონაცემების დათვალიერება?: '))
            if answer in ['კი', '']:
                query = ('Select * from oscar where age =?')
                c.execute(query, (age,))
                records = c.fetchall()
                print('მონაცემები ინახება შემდეგი სახით: (id, year, age, name, gender, movie)')
                for record in records:
                    print(record)
        continue_ans = str(input('გსურთ გაგრძელება?: '))
        if continue_ans in ['კი', '']:
            code = 1
        else:
            code = 0
    oscar_finish_incount()


# with this function  you can count data in oscar_db with sex(gender), for that you need to input sex(gender),
# then your answer will be sent in query, which will push with c.execute function. result
# will save in found var with fetchone function, and we will get only value with [0] index of
# values list from fetchone, program will ask you if you want to view the result, if answer will yes, then
# program will find this data with query and execute functions, and will print it. if user will want to continue code,
# he will answer 1 in answer input(str) var, then while cycle will repeat untill user will write something
# except 1 for leaving while cycle
def oscar_count_sex(conn=oscar_db_con()):
    code = 1
    c = conn.cursor()
    print('თქვენ აირჩიეთ მონაცემის დათვლა სქესის მიხედვით! მიყევით ინსტრუქციებს!')
    while code == 1:
        sex = str(input('რა სქესის ოსკარების მფლობლების დათვლა გსურთ?: '))
        if sex in ['F', 'f', 'FEMALE', 'female', 'Female']:
            sex = 'F'
        elif sex in ['M', 'm', 'MALE', 'male', 'Male']:
            sex = 'M'
        elif sex in ['Menu', 'menu', 'MENU']:
            oscar_finish_count()
        else:
            print('სულ ხელმისაწვდომია 2 გენდერი! Male/Female!')
            oscar_count_sex()
        query = ('Select count(*) from oscar where gender =?')
        c.execute(query, (sex,))
        found = c.fetchone()[0]
        print(f'მოიძებნა {found} მონაცემი.')
        if found != 0:
            answer = str(input('გსურთ მონაცემების დათვალიერება?: '))
            if answer in ['კი', '']:
                query = ('Select * from oscar where gender =?')
                c.execute(query, (sex,))
                records = c.fetchall()
                print('მონაცემები ინახება შემდეგი სახით: (id, year, age, name, gender, movie)')
                for record in records:
                    print(record)
        continue_ans = str(input('გსურთ გაგრძელება?: '))
        if continue_ans in ['კი', '']:
            code = 1
        else:
            code = 0
    oscar_finish_incount()


# with this function  you can count data in oscar_db with year interval, for that you need to input interval's start and stop,
# then your answer will be sent in query, which will push with c.execute function. result
# will save in found var with fetchone function, and we will get only value with [0] index of
# values list from fetchone, program will ask you if you want to view the result, if answer will yes, then
# program will find this data with query and execute functions, and will print it. if user will want to continue code,
# he will answer 1 in answer input(str) var, then while cycle will repeat untill user will write something
# except 1 for leaving while cycleg
def oscar_count_between(conn=oscar_db_con()):
    code = 1
    c = conn.cursor()
    print('თქვენ აირჩიეთ მონაცემის დათვლა დროის შუალედის მიხედვით! მიყევით ინსტრუქციებს!')
    while code == 1:
        year_start = int(input('შეიყვანის დროის შუალედის დასაწყისი: '))
        while year_start <= 1927:
            print('ოსკარები 1927 წლამდე არ არსებობს! სცადეთ სხვა თარიღი! ( 1928+ )')
            year_start = int(input('შეიყვანის დროის შუალედის დასაწყისი: '))
        year_stop = int(input('შეიყვანის დროის შუალედის დასასრული: '))
        query = ('Select count(*) from oscar where year between ? and ?')
        c.execute(query, (year_start, year_stop))
        found = c.fetchone()[0]
        print(f'მოიძებნა {found} მონაცემი.')
        if found != 0:
            answer = str(input('გსურთ მონაცემების დათვალიერება?: '))
            if answer in ['კი', '']:
                query = ('Select * from oscar where year between ? and ?')
                c.execute(query, (year_start, year_stop))
                records = c.fetchall()
                print('მონაცემები ინახება შემდეგი სახით: (id, year, age, name, gender, movie)')
                for record in records:
                    print(record)
        continue_ans = str(input('გსურთ გაგრძელება?: '))
        if continue_ans in ['კი', '']:
            code = 1
        else:
            code = 0
    oscar_finish_incount()


# with this function you can choose which count type you want to do, for that you need
# to input corresponding number in c var with input, then program will analyse your answer
# and will redirect you to the right function, if your choice will 0, program will close connection
# with database with c.close and will close code with sys.exit
def oscar_count_list(c=oscar_db_con()):
    print('თქვენ აირჩიეთ მონაცემების დათვლა! რის მიხედვით გსურთ დათვლა?')
    print('წელი(1) | ასაკი(2) | სქესი(3) | დროის შუალედი(4)| მენიუში დაბრუნება (5) | EXIT(0)')
    choice = str(input('შეიყვანეთ სასურველი მოქმედება: '))
    if choice == '1':
        oscar_count_year()
    elif choice == '2':
        oscar_count_age()
    elif choice == '3':
        oscar_count_sex()
    elif choice == '4':
        oscar_count_between()
    elif choice == '5':
        oscar_finish_count()
    elif choice == '0':
        print('მიმდინარეობს პროცესების შეწყვეტა...')
        time.sleep(1)
        c.close()
        sys.exit('Goodbye, dear friend!')


# this function is building diagramme with a sex(gender) data
def oscar_diagramme_sex(c=oscar_db_con().cursor()):
    # it's a query, which will sort data in db on 2 gender
    query = "Select count(*) from oscar where gender=?"
    # 1st gender will find with query and gender 'M' Female
    c.execute(query, ('F',))
    # program will catch data with this fetchone function's list's [0] index data, where will be our count
    f_count = c.fetchone()[0]
    # 2nd gender will find with query and gender 'M' Male
    c.execute(query, ('M',))
    # program will catch data with this fetchone function's list's [0] index data, where will be our count
    m_count = c.fetchone()[0]
    print('მიმდინარეობს მონაცემების დამუშავება...')
    # little sleep, like program is analysing data and searching something, or drinking coffe ;D
    time.sleep(1.5)
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = f'Man ({m_count})', f'Woman ({f_count})'
    # there's circle's part's sizes, it will be convert in %, 1% is 3.6 degree
    sizes = [m_count, f_count]
    # it's circle's part's explode, little 'departure' from the circle
    explode = (0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    # this function is calling upper code and is showing diagramme to us.
    plt.show()
    # that funtion is finishing this code and then it will redirect us to previous menu
    oscar_finish_diagramme()


# this function is building diagramme with a age data
def oscar_diagramme_age(c=oscar_db_con().cursor()):
    # this query is structure of searching, it counts results from execute, it will search data where age is between
    # first(?) placeholder and second placeholder(?)
    query = "Select count(*) from oscar where age between ? and ?"
    c.execute(query, ('0', '19'))
    count_0 = c.fetchone()[0]
    c.execute(query, ('20', '39'))
    count_1 = c.fetchone()[0]
    c.execute(query, ('40', '59'))
    count_2 = c.fetchone()[0]
    c.execute(query, ('60', '79'))
    count_3 = c.fetchone()[0]
    c.execute(query, ('80', '130'))
    count_4 = c.fetchone()[0]
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = f'0-19 ({count_0})', f'20-39 ({count_1})', f'40-59 ({count_2})', f'60-79 ({count_3})', f'80+ ({count_4})'
    sizes = [count_0, count_1, count_2, count_3, count_4]
    explode = (0, 0, 0, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()
    oscar_finish_diagramme()

    # this query is structure of searching, it counts results from execute, it will search data where age is between
    # first(?) placeholder and second placeholder(?), but now you will input age's intervals


def oscar_diagramme_age_manual(c=oscar_db_con().cursor()):
    first_start = int(input('შეიყვანეთ პირველი შუალედუს დასაწყისი: '))
    while first_start < 0:
        print('ასაკი უარყოფითი ვერ იქნება!')
        first_start = int(input('შეიყვანეთ პირველი შუალედუს დასაწყისი: '))
    first_stop = int(input('შეიყვანეთ პირველი შუალედის დასასრული: '))
    while (first_stop < 0 or first_stop <= first_start):
        print(f'ასაკი უარყოფითი, ან შუალედის დასაწყისის ნაკლები/ტოლი({first_start}) ვერ იქნება!')
        first_stop = int(input('შეიყვანეთ პირველი შუალედუს დასასრული: '))

    second_start = int(input('შეიყვანეთ მეორე შუალედუს დასაწყისი: '))
    while (second_start < 0 or second_start <= first_stop):
        print(f'ასაკი უარყოფითი, ან პირველი შუალედის დასასრულზე({first_stop}) ნაკლები ვერ იქნება!')
        second_start = int(input('შეიყვანეთ მეორე შუალედუს დასაწყისი: '))
    second_stop = int(input('შეიყვანეთ მეორეშუალედის დასასრული: '))
    while (second_stop < 0 or second_stop <= second_start):
        print(f'ასაკი უარყოფითი, ან შუალედის დასაწყისის ნაკლები/ტოლი({second_start}) ვერ იქნება!')
        second_stop = int(input('შეიყვანეთ მეორე შუალედუს დასასრული: '))
    query = "Select count(*) from oscar where age between ? and ?"
    c.execute(query, (str(first_start), str(first_stop)))
    count_0 = c.fetchone()[0]
    c.execute(query, (str(second_start), str(second_stop)))
    count_1 = c.fetchone()[0]
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = f'{first_start}-{first_stop} ({count_0})', f'{second_start}-{second_stop} ({count_1})'
    sizes = [count_0, count_1, ]
    explode = (0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()
    oscar_finish_diagramme()

    # this query is structure of searching, it counts results from execute, it will search data where year is between
    # first(?) placeholder and second placeholder(?)


def oscar_diagramme_year(c=oscar_db_con().cursor()):
    query = "Select count(*) from oscar where year between ? and ?"
    c.execute(query, ('1927', '1939'))
    count_0 = c.fetchone()[0]
    c.execute(query, ('1940', '1969'))
    count_1 = c.fetchone()[0]
    c.execute(query, ('1970', '1999'))
    count_2 = c.fetchone()[0]
    c.execute(query, ('2000', '2019'))
    count_3 = c.fetchone()[0]
    c.execute(query, ('2020', '2100'))
    count_4 = c.fetchone()[0]
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = f'1927-1939 ({count_0})', f'1940-1969 ({count_1})', f'1970-1999 ({count_2})', f'2000-2019 ({count_3})', f'2020+ ({count_4})'
    sizes = [count_0, count_1, count_2, count_3, count_4]
    explode = (0, 0, 0, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()
    oscar_finish_diagramme()

    # this query is structure of searching, it counts results from execute, it will search data where year is between
    # first(?) placeholder and second placeholder(?), but now you will input year's intervals in the code


def oscar_diagramme_year_manual(c=oscar_db_con().cursor()):
    first_start = int(input('შეიყვანეთ პირველი შუალედუს დასაწყისი: '))
    while first_start <= 1927:
        print('ოსკარები 1927 წლამდე არ არსებობს! სცადეთ სხვა თარიღი! ( 1928+ )')
        first_start = int(input('შეიყვანეთ პირველი შუალედუს დასაწყისი: '))
    first_stop = int(input('შეიყვანეთ პირველი შუალედის დასასრული: '))
    while (first_stop < 0 or first_stop <= first_start):
        print(f'თარიღი უარყოფითი, ან შუალედის დასაწყისის ნაკლები/ტოლი({first_start}) ვერ იქნება!')
        first_stop = int(input('შეიყვანეთ პირველი შუალედუს დასასრული: '))

    second_start = int(input('შეიყვანეთ მეორე შუალედუს დასაწყისი: '))
    while (second_start < 0 or second_start <= first_stop):
        print(f'თარიღი უარყოფითი, ან პირველი შუალედის დასასრულზე({first_stop}) ნაკლები ვერ იქნება!')
        second_start = int(input('შეიყვანეთ მეორე შუალედუს დასაწყისი: '))
    second_stop = int(input('შეიყვანეთ მეორეშუალედის დასასრული: '))
    while (second_stop < 0 or second_stop <= second_start):
        print(f'ასაკი უარყოფითი, ან შუალედის დასაწყისის ნაკლები/ტოლი({second_start}) ვერ იქნება!')
        second_stop = int(input('შეიყვანეთ მეორე შუალედუს დასასრული: '))
    query = "Select count(*) from oscar where year between ? and ?"
    c.execute(query, (str(first_start), str(first_stop)))
    count_0 = c.fetchone()[0]
    c.execute(query, (str(second_start), str(second_stop)))
    count_1 = c.fetchone()[0]
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = f'{first_start}-{first_stop} ({count_0})', f'{second_start}-{second_stop} ({count_1})'
    sizes = [count_0, count_1, ]
    explode = (0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()
    oscar_finish_diagramme()


# with this function you can choose which diagramme type you want to do, for that you need
# to input corresponding number in choice var with input, then program will analyse your answer
# and will redirect you to the right function, if your choice will 0, program will close connection
# with database with c.close and will close code with sys.exit
def oscar_diagramme_list(c=oscar_db_con()):
    print('თქვენ აირჩიეთ დიაგრემის აგება! ამისთვის მიყევით ინსტრუქციებს!')
    print('სქესის მიხედვით(1) | ასაკის შუალედები (2) | ასაკის შესაყვანი შუალედები (3) | თარიღის შუალედები(4) |'
          'თარიღის შესაყვანი შუალედები(5) | მენიუში დაბრუნება (6) | Exit (0)')
    choice = str(input('შეიყვანეთ სასურველი მოქმედება: '))
    if choice == '1':
        oscar_diagramme_sex()
    elif choice == '2':
        oscar_diagramme_age()
    elif choice == '3':
        oscar_diagramme_age_manual()
    elif choice == '4':
        oscar_diagramme_year()
    elif choice == '5':
        oscar_diagramme_year_manual()
    elif choice == '6':
        print('მიმდინაორებს მენიუში გადასვლა...')
        time.sleep(2)
        oscar_db_todo()
    elif choice == '0':
        print('მიმდინარეობს პროცესების შეწყვეტა...')
        time.sleep(1)
        c.close()
        sys.exit('Goodbye, dear friend!')


# 1+ 2+ 3+ 4+ 5+ 6- 7+ 0+

# this is main menu of Oscar_DB, here you can choose, what you want to do: sort/add/update/delete/count/diagramme
# or you want to return in program's main menu. program will ask you and you will input corresponding number
# then program will analyse your input and will redirect you to the right function, if you will choose 0,
# program will close connection(c.close) with database and will exit from the code with sys.exit
def oscar_db_todo(c=oscar_db_con()):
    print(
        'მონაცემების მოძებნა/სორტირება(1) | მონაცემების დამატება (2)| მონაცემების განახლება(3) | მონაცემების წაშლა(4) |'
        ' მონაცემების დათვლა(5) | დიაგრამის აგება(6) | მენიუში დაბრუნება(7) | EXIT (0)')
    choice = str(input('შეიყვანეთ სასურველი მოქმედება: '))
    if choice == '1':
        oscar_sort_list()
    elif choice == '2':
        oscar_add_person()
    elif choice == '3':
        oscar_update_p()
    elif choice == '4':
        oscar_delete_p()
    elif choice == '5':
        oscar_count_list()
    elif choice == '6':
        oscar_diagramme_list()
    elif choice == '7':
        print('მიმდინარეობს მთავარ მენიუში გადასვლა...')
        time.sleep(2)
        c.close()
        choice_db()
    elif choice == '0':
        c.close()
        sys.exit('Goodbye, dear friend!')
    else:
        print('დაფიქსირდა შეცდომა! ხელმისაწვდომია მხოლოდ ქვემოთ მოყვანილი მოქმედებები!')
        oscar_db_todo()


# that's welcome function, it was called when you choose Oscars in program's main menu, it will call 'what to do' function
def oscar_db():
    print('თქვენ აირჩიეთ Oscar Winners მონაცემთა ბაზა, თქვენ შეგიძლიათ აირჩიოთ შემდეგი მოქმედებები:')
    oscar_db_todo()


# that's the main menu of the program, where you can select database, if you will select 0, program will stop the code
# with sys.exit,
def choice_db():
    print('Oscar(1) | Movies(2) !Coming soon!| Exit(0)')
    choice = str(input('შეიყვანეთ სასურველი მოქმედება: '))
    if choice in ['Oscar', 'oscar', '1']:
        oscar_db()
    elif choice in ['Movies', 'movies', '2']:
        print('Coming soon...')
    elif choice in ['Exit', 'exit', '0']:
        sys.exit('Goodbye, dear friend!')
    else:
        print('დაფიქსირდა შეცდომა! ხელმისაწვდომია მხოლოდ ქვემოთ მოყვანილი მოქმედებები!')
        choice_db()

#small introduse, after which we called choice_db functhin
print('მოგესალმებით, ხელმისაწვდომია 2 მონაცემთა ბაზასთან მოქმედებები, რომელი გსურთ აირჩიოთ?')

choice_db()
