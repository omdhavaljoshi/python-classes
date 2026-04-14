import pygame,random
import sqlite3
pygame.init()
pygame.mixer.music.load(r"Pygame classes/Dino game/dino music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

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

# Background Images -->
bg = pygame.image.load(r"Pygame classes/Class 1/bg (1).png")
ground_img = pygame.image.load(r"Pygame classes/Dino game/ground.png")

# Variables -->
h,w = 800,800
clock = pygame.time.Clock()
groundx = 0
groundSpeed = 4
screen  = pygame.display.set_mode((w,h))
pygame.display.set_caption("Dino game")
dinoY = h-210
dinoX = 100
ground = h-150
obstacle_list = [r"Pygame classes/Dino game/cactus.png", r"Pygame classes/Dino game/spikes.png"]
obstacle_x = w-10
obstacle_y = ground-50
game_on_pause = True
spawn_obstacle = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_obstacle,1500)
score = 0
score_font = pygame.font.Font(None,30)
LOGINSCREEN = "login screen"
current_screen = LOGINSCREEN
current_user = ""
# Sprites -->
class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.run_image = []
        self.idle_image = []
        self.jump_image = []
        self.dead_image = []
        self.load_images()
        self.index = 0
        self.image = self.idle_image[0]
        self.rect = self.image.get_rect(center = (dinoX,dinoY))
        self.counter = 0
        self.dino_state = "idle"
        self.dino_on_ground = True
        self.dino_velocity_y = 0
        self.gravity = 1
        self.jump_power = -20
    
    def load_images(self):
        for i in range(1,9):
            self.image = pygame.image.load(r"Pygame classes/Dino game/Dino Images/Run "+f"({i}).png")
            self.image = pygame.transform.scale(self.image,(160,160))
            self.run_image.append(self.image)

        for i in range(1,11):
            self.image = pygame.image.load(r"Pygame classes/Dino game/Dino Images/Idle "+f"({i}).png")
            self.image = pygame.transform.scale(self.image,(160,160))
            self.idle_image.append(self.image)

        for i in range(1,13):
            self.image = pygame.image.load(r"Pygame classes/Dino game/Dino Images/Jump "+f"({i}).png")
            self.image = pygame.transform.scale(self.image,(160,160))
            self.jump_image.append(self.image)
        
        for i in range(1,9):
            self.image = pygame.image.load(r"Pygame classes/Dino game/Dino Images/Dead "+f"({i}).png")
            self.image = pygame.transform.scale(self.image,(160,160))
            self.dead_image.append(self.image)
    
    def track_counter(self):
        self.counter+=1
        if self.counter >= 8:
            self.counter = 0
            self.index += 1

    def run(self):
            self.track_counter()
            if self.index > len(self.run_image)-1:
                self.index = 0
            self.image = self.run_image[self.index]

    def idle_(self):
        self.track_counter()
        if self.index > len(self.idle_image)-1:
            self.index = 0
        self.image = self.idle_image[self.index]
    
    def gravity_handle(self):
        self.rect.y += self.dino_velocity_y 
        self.dino_velocity_y += self.gravity 
        if self.rect.y >= 510:
            self.dino_state = "run"
            self.dino_velocity_y = 0
            self.rect.y = 510
            self.dino_on_ground = True

    def start_jump(self):
        if self.dino_on_ground == True:
            self.dino_on_ground = False
            self.dino_velocity_y = self.jump_power
            self.dino_state = "jump"

    def jump(self):
        self.track_counter()
        if self.index >= len(self.jump_image):
            self.index = 0
        self.image = self.jump_image[self.index]
        self.gravity_handle()
    
    def death(self):
        self.track_counter()
        if self.index > len(self.dead_image)-1:
            self.index = 0
        if self.index >= len(self.dead_image)-1:
            self.dino_state = "idle"
        self.image = self.dead_image[self.index]
       
    def update(self):
        if self.dino_state == "idle":
            self.idle_()
        elif self.dino_state == "run":
            self.run()
        elif self.dino_state == "jump":
            self.jump()
        elif self.dino_state == "dead":
            self.death()

class Obstacles(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(random.choice(obstacle_list))
        self.image = pygame.transform.scale(self.image,(70,100))
        self.rect = self.image.get_rect(center = (obstacle_x,obstacle_y))
        self.speed = 4

    def move_left(self):
        global score
        if dino.dino_on_ground == True:
            self.rect.x -= self.speed
            if self.rect.right< dino.rect.left:
                self.kill()
                score +=1
        else:
            self.rect.x -= self.speed+0.7
            if self.rect.right< dino.rect.left:
                self.kill()
                score +=1

    def update(self):
        if game_on_pause == False:
            self.move_left()

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
        
dino = Dino()
player_group = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()
player_group.add(dino)

runninStatus = True
while runninStatus:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runninStatus = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                dino.dino_state = "run"
                game_on_pause = False
            if event.key == pygame.K_SPACE:
                dino.start_jump()
                game_on_pause = False
            # if event.key == pygame.K_d:
            #     dino.dino_state = "dead"
            #     game_on_pause = True
        if event.type == spawn_obstacle and game_on_pause == False:
            obstacle_group.add(Obstacles())
            
    if current_screen == LOGINSCREEN:
        authenticate()
        print("test")

    # if current_screen == "loged_in":
    #     # continue
    # Collision -->
    if pygame.sprite.spritecollide(dino,obstacle_group,False,pygame.sprite.collide_mask):
        game_on_pause = True
        dino.dino_state = "dead"
        save_score(current_user)

    # Scroll Logic -->
    if game_on_pause == False:
        if dino.dino_on_ground == True:
            groundx -= groundSpeed
            if groundx <= -102:
                groundx = 0
        else:
            groundx -= groundSpeed+0.7
            if groundx <= -102:
                groundx = 0
    
    screen.blit(bg,(0,0))
    screen.blit(ground_img,(groundx,h-150))
    player_group.draw(screen)
    player_group.update()
    obstacle_group.draw(screen)
    obstacle_group.update()
    score_text = score_font.render(f"Score : {score}",False,"BLACK")
    screen.blit(score_text,(10,10))

    pygame.display.update()

pygame.quit()