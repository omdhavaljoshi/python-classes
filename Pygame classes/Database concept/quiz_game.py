import sqlite3

connection = sqlite3.connect(r"Database concept/database.db")
cursor = connection.cursor()

# Creating the table -->
cursor.execute("""
CREATE TABLE IF NOT EXISTS quiz(
               sn INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               score INTEGER)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_login(
               sn INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               user_id TEXT UNIQUE,
               password TEXT)
""")
# Variables -->
signed_in = False
user_score = 0
name = None

# Functions -->
def create_account():
    name = input("What is your name: ")
    user_id = input("Create a user id: ")
    password = input("Create a password: ")
    cursor.execute("""INSERT INTO user_login(name,user_id,password) VALUES(?,?,?)""",(name,user_id,password))
    print("Account has been created successfully.")
    connection.commit()

def sign_in():
    global signed_in
    signin_userid = input("What is you user id: ")
    signin_password = input("What is your password: ")
    cursor.execute("""SELECT user_id,password from user_login WHERE user_id = ? AND password = ?""",(signin_userid,signin_password))
    data = cursor.fetchall()
    for item in data:
        print(item)
        if item[0] == signin_userid and item[1] == signin_password:
            print("Login successful!")
            signed_in = True
        else:
            print("User id or password is incorrect.")
            signed_in = False

def play_quiz(user_name):
    python_questions = [
{
"question": "Which keyword is used to define a function in Python?",
"options": ["A. function", "B. define", "C. def", "D. func"],
"answer": "C"
},
{
"question": "Which data type stores True or False?",
"options": ["A. int", "B. bool", "C. str", "D. float"],
"answer": "B"
},
{
"question": "What will print(len('Hello')) output?",
"options": ["A. 4", "B. 5", "C. 6", "D. Error"],
"answer": "B"
},
{
"question": "Which symbol is used for comments in Python?",
"options": ["A. //", "B. #", "C. /* */", "D. --"],
"answer": "B"
},
{
"question": "Which function takes input from user?",
"options": ["A. scan()", "B. read()", "C. input()", "D. get()"],
"answer": "C"
},
{
"question": "Which data structure stores multiple values?",
"options": ["A. list", "B. int", "C. float", "D. bool"],
"answer": "A"
},
{
"question": "What is the index of first element in Python list?",
"options": ["A. 0", "B. 1", "C. -1", "D. 2"],
"answer": "A"
},
{
"question": "Which loop runs while a condition is true?",
"options": ["A. for", "B. while", "C. loop", "D. repeat"],
"answer": "B"
},
{
"question": "Which keyword stops a loop?",
"options": ["A. stop", "B. break", "C. exit", "D. halt"],
"answer": "B"
},
{
"question": "Which library is used for databases like SQLite?",
"options": ["A. pandas", "B. sqlite3", "C. numpy", "D. turtle"],
"answer": "B"
}
]
    for i in range(len(python_questions)):
        print(python_questions[i]["question"])
        print(python_questions[i]["options"])
        user_answer = input("Answer: ")
        if user_answer == python_questions[i]["answer"]:
            user_score += 1
    cursor.execute("""INSERT INTO quiz(score) VALUES(?) WHERE user_id = ?""",(user_score,user_name))

# Start of game -->
while True:
    print("""
    1. Create Account
    2. Sign in
    3. Exit
""")
    choice = input("Choose what you want to do: ")
    if choice == '3':
        break
    elif choice == '2':
        sign_in()
    elif choice == '1':
        create_account()
    if signed_in:
        print("""
              1. Play Quiz
              2. Show my scores
              3. Show all scores
              4. Show Maximum scores
              5. Sow top 2 scores
              6. Logout""")
        quiz_choice = input("Choose what you want to do: ")
        if quiz_choice == 1:
            play_quiz()