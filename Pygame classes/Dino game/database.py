import sqlite3
from Dino_game import score

connection = sqlite3.connect(r"/Users/omjoshi/Library/CloudStorage/OneDrive-Personal/Coding/Python coding class/Pygame classes/Database concept/database.db")
cursor = connection.cursor()

# Creating the table -->
cursor.execute("""
CREATE TABLE IF NOT EXISTS dino_game(
               sn INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               user_id TEXT,
               score INTEGER)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_login_dinogame(
               sn INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               user_id TEXT,
               password TEXT)
""")

def save_score(current_user):
    cursor.execute("""SELECT score FROM dino_game WHERE user_id = ?""", (current_user,))
    current_score = cursor.fetchall()
    if score > current_score[0][0]:
        cursor.execute("""UPDATE dino_game SET score = ? WHERE user_id = ?""", (score,current_user))
        connection.commit()
        print("Score updated")
        print(current_score[0][0])
        cursor.execute("""SELECT score FROM dino_game WHERE user_id = ?""", (current_user,))
        updated_score = cursor.fetchall()
        print(updated_score[0][0])