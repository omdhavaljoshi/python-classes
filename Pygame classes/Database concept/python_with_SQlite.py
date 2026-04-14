import sqlite3

connections = sqlite3.connect(r"Database concept/database.db")
print(connections)
cursor = connections.cursor()

# Creating table -->
cursor.execute("""
CREATE TABLE IF NOT EXISTS activity(
               sn INTERGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               score INTEGER
               )
""")

# Whenever you perform create, delete, update, insert using cursor you always have to commit.

# Functions -->
def insert_data():
    name = input("Enter your name: ")
    score = int(input("Enter your score: "))
    cursor.execute("""INSERT INTO activity(name,score) VALUES(?,?)""",(name,score))
    connections.commit()

def delete_data():
    delete_sn = int(input("What SN value do you want to delete: "))
    cursor.execute("""DELETE FROM activity() WHERE sn = ?""",(delete_sn,))
    connections.commit()

def update_data():
    update_value = int(input("What is the SN value of the row you want to update: "))
    update_what = input("What do you want to update(name/score): ")
    if update_what == 'name':
        update_to = input("what do you want to update it to: ")
    else:
        update_to = int(input("what do you want to update it to: "))
    cursor.execute("""UPDATE activity() SET ? = ? WHERE sn = ?""",(update_what,update_to,update_value))
while True:
    print("""
--------------- Menu ---------------
        1. Insert Data
        2. Delete Data
        3. Update Data
        4. Fetch Data
        5. Exit
""")
    choice = int(input("Enter your choice: "))
    if choice == 5:
        break
    elif choice == 1:
        insert_data()
    elif choice == 2:
        delete_data()
    elif choice == 3:
        update_data()