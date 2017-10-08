import pymysql.cursors

connect = pymysql.connect(host='localhost',
                          user='root',
                          password='welcome001',
                          db='udit')

cursor = connect.cursor()

def set_id():
    query = 'select max(id) from udit.username'
    cursor.execute(query)
    connect.commit()

    result = cursor.fetchall()
    for row in result:
        id_count = row[0]
        break
    return id_count

def username_db():
    query = 'select * from udit.username'
    cursor.execute(query)
    connect.commit()

    result = cursor.fetchall()
    print(result)

def entry():
    username = input("Please enter your username: ")
    username = "'" + username + "'"
    query = 'select * from udit.username where username = {}'.format(username)
    cursor.execute(query)
    connect.commit()

    result = cursor.fetchall()
    for row in result:
        user_id = row[0]
    return (user_id)


def user_new(user_id):
    user_new = input("Welcome new user! \nPlease enter a username: ")
    user_new = "'" + user_new + "'"
    user_id += 1
    
    query =('insert into udit.username (id, username) values ({}, {})'.format(user_id, user_new))
    cursor.execute(query)
    connect.commit()
    
    query1 = 'select * from udit.username order by id desc'
    cursor.execute(query1)

    result = cursor.fetchall()
    for row in result:
        result2 = row
        break
    
    return result2

def user_update():
    username_old = input("Please enter your current username: ")
    username_old = "'" + username_old + "'"

    username_new = input("Please enter your new username: ")
    user_in = username_new
    username_new = "'" + username_new + "'"

    query = 'update udit.username set username = {} where username = {}'.format(username_new, username_old)
    cursor.execute(query)
    connect.commit()

    query1 = 'select * from udit.username'
    cursor.execute(query1)
    
    result = cursor.fetchall()
    
    for row in result:
        if row[1] == user_in:
            return row
        else:
            pass
        
def schedule():
    key = entry()
    while True:
        slot_entry = input("Please enter the event: ")
        slot_entry = "'" + slot_entry + "'"
        
        query = 'insert into udit.py_schedule (id, new_in) values ({}, {})'.format(key, slot_entry)
        cursor.execute(query)
        connect.commit()

        user_in = input("Would you like to continue entering?\nEnter y for yes and n for no: ")
        if user_in == 'y':
            pass
        
        elif user_in == 'n':
            break
        
        else:
            print("invalid input...\nEnter y for yes and n for no: ")
            pass

def check_schedule():
    user_id = entry()
    query = 'select * from udit.py_schedule where id = {}'.format(user_id)
    cursor.execute(query)
    connect.commit()

    result = cursor.fetchall()

    print("\n")
    print("Your schedule:")
    for row in result:
        print(row[1])
    print("\n")

def del_user():
    user_in = input("Are you sure you want to delete your profile?\nPlease type yes or no: ")
    if user_in == "yes":
        user_id = entry()
        query = 'delete from udit.username where id = {}'.format(user_id)
        query1 = 'delete from udit.py_schedule where id = {}'.format(user_id)

        cursor.execute(query)
        connect.commit()

        cursor.execute(query1)
        connect.commit()
        print("Your profile was succesfully deleted.")
    elif user_in == "no":
        pass
    else:
        print("invalid input... please type yes or no: ")
    

def main():
    print("Welcome to my database function!\n")
    functions = """0: display users
1: new user
2: update user
3: create schedule
4: check schedule
5: delete user
6: end
"""
    user_id = set_id()

    while True:
        print(functions)
        user_in = input("Please enter function: ")
        if user_in == "0":
            query = 'select * from udit.username'
            cursor.execute(query)
            connect.commit()
            result = cursor.fetchall()
            for row in result:
                print(row[1])
        elif user_in == "1":
            user_info = user_new(user_id)
            print(user_info)
        elif user_in == "2":
            user_info = user_update()
            print("Your username was successfully changed.")
            print("Your new username is {}".format(user_info[1]))
            print("Your new id is {}".format(user_info[0]))
        elif user_in == "3":
            schedule()
        elif user_in == "4":
            check_schedule()
        elif user_in == "5":
            del_user()
        elif user_in == "6":
            break
        else:
            print("Input not valid; please try again")
            pass
        
main()
    
