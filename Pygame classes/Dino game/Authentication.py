import database as d
import settings as s

def create_account():
        name = input("What is your name: ")
        d.cursor.execute("""SELECT user_id FROM user_login_dinogame""")
        user_ids = d.cursor.fetchall()
        while True:
            user_id = input("Select a user_id: ")
            print(user_ids)
            if user_id in user_ids[0]:
                print("Make a unique user id.") 
            else:
                password = input("Choose a password: ")
                d.cursor.execute("""INSERT INTO user_login_dinogame(name,user_id,password) VALUES(?,?,?)""",(name,user_id,password))
                print("Account successfully created")
                d.cursor.execute("""INSERT INTO dino_game(name,user_id,score) VALUES(?,?,?)""", (name,user_id,0))
                authenticate()
                d.connection.commit()
                break

def sign_in():
    # global s.current_screen, s.current_user
    user_name = input("What is your user id: ")
    password = input("What is your password: ")
    d.cursor.execute("""SELECT user_id,password FROM user_login_dinogame WHERE user_id = ? AND password = ?""", (user_name,password))
    login_data = d.cursor.fetchall()
    if len(login_data) > 0:
        print("Successfully loged in.")
        s.current_screen = s.MENUSCREEN
        s.current_user = user_name
        return
    else:
        print("Password or User id incorrect")
        # authenticate()

def authenticate():
    print("""
    1. Create Account
    2. Sign in
    3. Exit
""")
    choice = input("Select a option: ")
    if choice == '1':
        create_account()
    elif choice == '2':
        sign_in()
    elif choice =='3':
        return