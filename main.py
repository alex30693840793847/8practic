import sqlite3

con = sqlite3.connect('8lab.db')
cursor = con.cursor()

cursor.execute(
    '''Create table if not exists _GROUP(
    id integer primary key autoincrement,
    name text,
    balance integer)''')

cursor.execute(
    '''Create table if not exists USER(
    id integer primary key autoincrement,
    name text,
    email text,
    member_since text,
    avatar text)''')

cursor.execute(
    '''Create table if not exists GROUP_USER(
    id integer primary key autoincrement,
    id_group integer references _GROUP(id),
    id_user integer references USER(id),
    balance integer)''')

cursor.execute(
    '''Create table if not exists BILL(
    id integer primary key autoincrement,
    id_group integer references _GROUP(id),
    title integer,
    amount integer,
    date text,
    created_by integer)''')

cursor.execute(
    '''Create table if not exists BILL_USER_OWES(
    id integer primary key autoincrement,
    id_bill integer references BILL(id),
    id_user integer references USER(id),
    owes integer)''')

cursor.execute(
    '''Create table if not exists BILL_USER_PAID(
    id integer primary key autoincrement,
    id_bill integer references BILL(id),
    id_user integer references USER(id),
    paid integer)''')

cursor.execute(
    '''Create table if not exists NOTE(
    id integer primary key autoincrement,
    id_bill integer references BILL(id),
    id_user integer references USER(id),
    massage text,
    created text)''')

print('1 - добавление; 2 - вывод таблиц')
choice = int(input())

if choice == 1:
    print('1 - group; 2 - bill; 3 - group_user; 4 - bill_user_owes; 5 - bill_user_paid; 6 - note; 7 - user;')
    table_choice = int(input())
    if table_choice == 1:
        name = input('имя: ')
        balance = input('баланс: ')
        cursor.execute('''insert into _GROUP(name, balance) values(?, ?);''', (name, balance))
    elif table_choice == 2:
        id_group = input('id группы: ')
        title = input('название: ')
        amount = input('сумма: ')
        date = input('дата: ')
        created_by = input('создатель: ')
        cursor.execute('''insert into BILL(id_group, title, amount, date, created_by) values(?, ?, ?, ?, ?);''',
                       (id_group, title, amount, date, created_by))
    elif table_choice == 3:
        id_group = input('id группы: ')
        id_user = input('id пользователя: ')
        balance = input('баланс: ')
        cursor.execute('''insert into GROUP_USER(id_group, id_user, balance) values(?, ?, ?);''', (id_group, id_user, balance))
    elif table_choice == 4:
        id_bill = input('id счета: ')
        id_user = input('id пользователя: ')
        owes = input('долг: ')
        cursor.execute('''insert into BILL_USER_OWES(id_bill, id_user, owes) values(?, ?, ?);''', (id_bill, id_user, owes))
    elif table_choice == 5:
        id_bill = input('id счета: ')
        id_user = input('id пользователя: ')
        paid = input('оплачено: ')
        cursor.execute('''insert into BILL_USER_PAID(id_bill, id_user, paid) values(?, ?, ?);''', (id_bill, id_user, paid))
    elif table_choice == 6:
        id_bill = input('id счета: ')
        id_user = input('id пользователя: ')
        message = input('сообщение: ')
        created = input('дата создания: ')
        cursor.execute('''insert into NOTE(id_bill, id_user, message, created) values(?, ?, ?, ?);''', (id_bill, id_user, message, created))
    elif table_choice == 7:
        name = input('имя: ')
        email = input('почта: ')
        member_since = input('дата регистрации: ')
        avatar = input('аватар: ')
        cursor.execute('''insert into USER(name, email, member_since, avatar) values(?, ?, ?, ?);''', (name, email, member_since, avatar))
    else:
        print('Неверный выбор.')

    con.commit()

elif choice == 2:
    print('1 - group; 2 - bill; 3 - group_user; 4 - bill_user_owes; 5 - bill_user_paid; 6 - note; 7 - user;')
    table_choice = int(input())

    if table_choice == 1:
        cursor.execute('''select * from _GROUP''')
    elif table_choice == 2:
        cursor.execute('''select * from BILL''')
    elif table_choice == 3:
        cursor.execute('''select * from GROUP_USER''')
    elif table_choice == 4:
        cursor.execute('''select * from BILL_USER_OWES''')
    elif table_choice == 5:
        cursor.execute('''select * from BILL_USER_PAID''')
    elif table_choice == 6:
        cursor.execute('''select * from NOTE''')
    elif table_choice == 7:
        cursor.execute('''select * from USER''')
    else:
        print('Неверный выбор.')

    data = cursor.fetchall()
    for row in data:
        print(row)

con.close()
