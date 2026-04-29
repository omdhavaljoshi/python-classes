from database import cursor,connection

def create_account():
        name = input("What is your name: ")
        cursor.execute("""SELECT user_id FROM user_login_dinogame""")
        user_ids = cursor.fetchall()
        while True:
            user_id = input("Select a user_id: ")
            print(user_ids)
            if user_id in user_ids[0]:
                print("Make a unique user id.")
            else:
                password = input("Choose a password: ")
                cursor.execute("""INSERT INTO user_login_dinogame(name,user_id,password) VALUES(?,?,?)""",(name,user_id,password))
                connection.commit()
                print("Account successfully created")
                cursor.execute("""INSERT INTO dino_game(name,user_id,score) VALUES(?,?,?)""", (name,user_id,0))
                authenticate()
                break

def sign_in():
    global current_screen, current_user
    user_name = input("What is your user id: ")
    password = input("What is your password: ")
    cursor.execute("""SELECT user_id,password FROM user_login_dinogame WHERE user_id = ? AND password = ?""", (user_name,password))
    login_data = cursor.fetchall()
    if len(login_data) > 0:
        print("Successfully loged in.")
        current_screen = "loged_in"
        current_user = user_name
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