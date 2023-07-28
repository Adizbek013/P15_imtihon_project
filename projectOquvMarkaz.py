import sqlite3
import hashlib


def hash_password(text: str):
    sha256 = hashlib.sha256()
    sha256.update(text.encode('utf-8'))
    return sha256.hexdigest()


def con():
    return sqlite3.connect('imtihon.db')


def create_table_oquvmarkaz():
    conn = con()
    cur = conn.cursor()
    cur.execute("""
        create table if not exists oquvmarkaz (
            userID integer primary key autoincrement,
            first_name varchar(30), 
            last_name varchar(30),
            birth_day date,
            phone varchar(13),
            username varchar(50),
            password varchar(150),
            is_admin default False
        )
    """)
    conn.commit()
    conn.close()


def create_table_kurs():
    conn = con()
    cur = conn.cursor()
    cur.execute("""
        create table if not exists kurs (
            courseID integer primary key,
            name varchar(50),
            number_of_students integer,
            is_active boolean 
        )
    """)
    conn.commit()
    conn.close()


def add_course(data1: dict):
    conn = con()
    cur = conn.cursor()
    query = """
        insert into kurs (name, number_of_students, is_active)
        values (?, ?, ?)
    """
    values = (data1['name'], data1['number_of_students'], data1['is_active'])
    cur.execute(query, values)
    print("Kurs qo'shildi")
    conn.commit()
    conn.close()


def add_user(data2: dict):
    conn = con()
    cur = conn.cursor()
    hashed_password = hash_password(data2['password'])
    query = """
        insert into oquvmarkaz (first_name, last_name, birth_day, phone, username, password, is_admin)
        values (?, ?, ?, ?, ?, ?, ?)
    """
    values = (data2['first_name'], data2['last_name'], data2['birth_day'], data2['phone'], data2['username'], hashed_password, data2['is_admin'])
    cur.execute(query, values)
    conn.commit()
    conn.close()


def get_userid(username: str, password: str):
    hashed_password = hash_password(password)
    conn = con()
    cur = conn.cursor()
    query = """
        select userID from oquvmarkaz 
        where username=? and password=?
    """
    values = (username, hashed_password)
    cur.execute(query, values)
    try:
        pk = cur.fetchall()[0]
        print("Login success")
    except IndexError:
        print("Login failed")
        pk = 0
    conn.close()
    return pk


def user_is_exist(a, b):
    query = f"""
        select count(userID) from oquvmarkaz 
        where {a}=?
    """
    value = (b,)
    conn = con()
    cur = conn.cursor()
    cur.execute(query, value)
    return cur.fetchall()


def show_courses():
    conn = con()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM kurs
    """)
    return cur.fetchall()



















