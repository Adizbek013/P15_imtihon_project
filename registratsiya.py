from projectOquvMarkaz import get_userid, user_is_exist, add_user, show_courses, add_course, con
from datetime import datetime

def login():
    username = input("Username kiriting :")
    password = input("Password kiriting :")
    pk = get_userid(username, password)
    return pk


def register():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    birth_day = input("Birthday: ")
    phone = input("Phone: ")
    username = input("Username: ")
    password1 = input("Password: ")
    password2 = input("Confirm password: ")
    if password1 == password2:
        if user_is_exist('username', username):
            print("Bu username band! ")
            return False
        data2 = dict(
            first_name=first_name,
            last_name=last_name,
            birth_day=birth_day,
            phone=phone,
            username=username,
            password=password1,
            is_admin=0
        )
        add_user(data2)
        print("Success! ")


def kursga_qoshilish(a, b, c):
    conn = con()
    cur = conn.cursor()
    cur.execute("""
        insert into lists (user_id, course_id, time)
        values (?, ?, ?)
    """, (a, b, c))
    conn.commit()
    conn.close()



def menu_talaba():
    print("1 -> Aktiv kurslar ro'yxatini ko'rish.")
    print("2 -> Aktiv kurslarga yozilish.")
    print("3 -> O'zi yozilgan kurslar ro'yxatini ko'rish.")
    tanlov = int(input("Tanlang: "))
    print( )
    if tanlov == 1:
        courses = show_courses()
        if courses:
            print("Courses")
            for i in courses:
                if i[3] == 1:
                    print(f"ID {i[0]} nomi {i[1]} qabul soni {i[2]}")
            print( )
            menu_talaba()

    elif tanlov == 2:
        courses = show_courses()
        if courses:
            print("Courses")
            for i in courses:
                if i[3] == 1:
                    print(f"ID {i[0]} nomi {i[1]} qabul soni {i[2]}")
            w = int(input("Kurs ID tanlang: "))
            kursga_qoshilish(w, datetime.now())




def menu_mentor():
    print("1 -> Kurs qo'shish.")
    print("2 -> Kursga yozilgan o'quvchilar ro'yxatini ko'rish.")
    print("3 -> Chiqish.")
    choise = int(input("Tanlang: "))
    if choise == 1:
        name = input("Course name: ")
        number_of_students = int(input("Number of students: "))
        data1 = dict(
            name=name,
            number_of_students=number_of_students,
            is_active=1
        )
        add_course(data1)
        menu_mentor()
    elif choise == 2:
        pass
    elif choise == 3:
        return "Xayr"



def menu():
    print("1 -> Register.")
    print("2 -> Talaba Login.")
    print("3 -> Mentor Login.")
    m = int(input("Tanlang: "))
    if m == 1:
        val = register()
        menu_talaba()
    elif m == 2:
        val = login()
        if val == 0:
            menu()
        else:
            menu_talaba()
    elif m == 3:
        val = login()
        if val == 0:
            menu()
        else:
            menu_mentor()
    else:
        print("Error!")
        menu()


menu()


