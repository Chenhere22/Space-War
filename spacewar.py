import turtle
import random
import time
from playsound import playsound
import tkinter as tk
from PIL import Image, ImageTk

from threading import Thread

# Initialize the turtle screen
turtle.fd(0)
turtle.speed(0)
turtle.bgcolor("black")
# Hide default turtle
turtle.ht()
#change window title
turtle.title("SpaceWar")
#change background
turtle.bgpic("bg.gif")
# This speeds up drawing
turtle.tracer(0)


# Sprite class definition
class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape=spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.goto(startx, starty)
        self.speed_value = 1  # Avoid name collision with turtle's speed method

    def move(self):
        self.fd(self.speed_value)
        # Boundary detection (optional, keeps the turtle in bounds)
        if self.xcor() > 290:
            self.setx(290)
            self.rt(60)
        if self.xcor() < -290:
            self.setx(-290)
            self.rt(60)
        if self.ycor() > 290:
            self.sety(290)
            self.rt(60)
        if self.ycor() < -290:
            self.sety(-290)
            self.rt(60)

    # Adjust the collision distance based on the turtle's size
    def is_collision(self, other):
        distance = self.distance(other)
        if distance < 20:  # Collision threshold (adjust this if needed)
            return True
        else:
            return False

# Player class inheriting from Sprite
class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid = 0.6, stretch_len= 1.1, outline=None)
        self.speed_value = 4
        self.lives = 3

    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)

    def accelerate(self):
        self.speed_value += 1  # Increase speed when up is pressed

    def decelerate(self):
        self.speed_value = max(0, self.speed_value - 1)  # Decrease speed when down is pressed

def playMissleFunc():
    playsound(r"missile.wav", block=True)

def playMissle():
    Thread(target=playMissleFunc).start()

def playCrashFunc():
    playsound(r"crash.wav", block=True)

def playCrash():
    Thread(target=playCrashFunc).start()

class Enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)    
        self.speed_value = 6 
        self.setheading(random.randint(0,360))

class Particle(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty) 
        self.shapesize(stretch_len=0.1, stretch_wid=0.1, outline= None)   
        self.goto(-1000,-1000)
        self.frame =0

    def explode(self, startx,starty, shape="circle"):
        self.shape(shape)
        self.goto(startx,starty)
        self.setheading(random.randint(0,360))    
        self.frame = 1

    def move(self):
        if self.frame > 0:
            self.fd(10)
            self.frame += 1

        if self.frame > 15:
            self.frame =0
            self.goto(-1000,-1000)



class Ally(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)    
        self.speed_value = 8 
        self.setheading(random.randint(0,360))

    def move(self):
        self.fd(self.speed_value)
        # Boundary detection (optional, keeps the turtle in bounds)
        if self.xcor() > 290:
            self.setx(290)
            self.lt(60)
        if self.xcor() < -290:
            self.setx(-290)
            self.lt(60)
        if self.ycor() > 290:
            self.sety(290)
            self.lt(60)
        if self.ycor() < -290:
            self.sety(-290)
            self.lt(60)

class Missile(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty) 
        self.shapesize(stretch_len=0.4, stretch_wid=0.2, outline=None)
        self.speed_value = 20
        self.status= "ready"
        self.goto(-1000,1000)
    
    def fire(self):
        if self.status == "ready":
            playMissle()
            self.status= "firing"
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())

    def move(self):
        if self.status =="ready":
            self.goto(-1000,1000)

        if self.status == "firing": 
            self.fd(self.speed_value)
        #border check
        if self.xcor()<-290 or self.xcor()>290 or \
        self.ycor() < -290 or self.ycor()>290:
            self.goto(-1000,1000)
            self.status ="ready"

class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.enemies_hit =0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3

    def draw_border(self):
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()
        self.pen.pendown()

    def show_status(self):
        self.pen.undo()
        msg=f"Score:{self.score}    Enemies Hit:{self.enemies_hit}"
        self.pen.penup()
        self.pen.goto(-300,310)
        self.pen.write(msg, font=("Arial", 12,"normal"))

    def game_over(self):
        self.state = "game_over"
        self.pen.clear()
        self.pen.penup()
        self.pen.goto(0,0)
        self.pen.write("Game Over", align="center", font=("Arial", 36,"bold"))
        self.pen.goto(0,-40)
        self.pen.write(f"Final Score:{self.score}", align="center", font=("Arial", 24, "normal") )   
        turtle.update()



game = Game()
game.draw_border()

#show the game status
game.show_status()

# Create player sprite
player = Player("triangle", "white", 0, 0)
missile = Missile("triangle", "yellow", 0, 0)

enemies = []
for i in range(6):
    enemies.append(Enemy("circle", "red", -100, 0))

allies = []
for i in range(6):
    allies.append(Ally("square", "blue", 100, 0))

particles=[]
for i in range(20):
    particles.append(Particle("circle", "orange", 0, 0))

# Keyboard bindings
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")  # Accelerate on Up arrow
turtle.onkey(player.decelerate, "Down")  # Decelerate on Down arrow
turtle.onkey(missile.fire, "space")
turtle.listen()

# Update player and enemy movement regularly
def game_loop():
    if game.state=="game_over":
        return 
    turtle.update()
    time.sleep(0.02)
    
    player.move()  # Player movement based on current speed_value
    missile.move()  # Missile movement

    # Collision detection 
    for enemy in enemies:
        enemy.move()
        if player.is_collision(enemy):
            playMissle()
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
            missile.status = "ready" 
            #increase score
            game.score -= 100
            game.show_status()
            
            collision_x, collision_y = player.xcor(), player.ycor()

            #do explosion
            for particle in particles:
                particle.explode(collision_x, collision_y, shape="triangle")
        
        #check for a collision between missile and enemy
        if missile.is_collision(enemy):
            playMissle()
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
            game.score += 100
            game.enemies_hit += 1
            game.show_status()

            #do explosion
            for particle in particles:
                particle.explode(missile.xcor(), missile.ycor(), shape="circle")


    for ally in allies:
        ally.move()
        
        if missile.is_collision(ally):
            playCrash()
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
            missile.status = "ready" 
            #increase score
            game.score -= 50
            game.show_status()        

    for  particle in particles:
        particle.move() 
    
    if game.score < -500:
        game.game_over()
    
    if game.state =="playing":
    # Schedule the next frame of the game loop
        turtle.ontimer(game_loop, 20)  # Call game_loop every 20 milliseconds

game_loop()
turtle.mainloop()