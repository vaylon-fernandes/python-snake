import turtle
import time
from random import randint
from tkinter import messagebox

delay = 0.1
score = 0
high_score = 0

#Screen Setup
win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("black")
win.setup(width=600,height=600)
win.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,100)
head.direction = "stop"


    
#snake food 
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(0.50,0.50)
food.goto(0,0)

#scoreboard
write_score = turtle.Turtle()
write_score.speed(0)
write_score.color("white")
write_score.penup()
write_score.shape("square")
write_score.hideturtle()
write_score.goto(0,250)
write_score.write(f"Score {score}  High Score: {high_score}",align = "center",font=("arial",24,"bold"))

def go_up():
  if head.direction != "down":
    head.direction = "up"

def go_down():
  if head.direction != "up":
    head.direction = "down"

def go_right():
  if head.direction != "left":
    head.direction = "right"
def go_left():
  if head.direction != "right":
    head.direction = "left"

def move():
  if head.direction == "up":
    y = head.ycor()
    head.sety(y+20)

  if head.direction =="down":
    y = head.ycor()
    head.sety(y-20)

  if head.direction=="right":
    x = head.xcor()
    head.setx(x+20)

  if head.direction=="left":
    x = head.xcor()
    head.setx(x-20)
    
def update_score(score,high_score):
  write_score.clear()
  write_score.write(f"Score {score}  High Score: {high_score}",align = "center",font=("arial",24,"bold"))
  
def game_over():
  
  global score
  global high_score
  
  for segment in segments:
    segment.goto(1000,100)
  segments.clear()
  messagebox.showinfo("Game over.",f"Your Score was {score}")
  score = 0
  
  update_score(score,high_score)
  
#action listeners
win.listen()
win.onkey(go_up,"w")
win.onkey(go_down,"s")
win.onkey(go_right,"d")
win.onkey(go_left,"a")



#array for snake body
segments = []

  
#update window continuosly
while True:
  win.update()
  
  
  #boundary collision
  if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
    time.sleep(1)
    head.goto(0,100)
    head.direction = "stop"
    x = randint(-290,290)
    y = randint(-290,290) 
    food.goto(x,y)

    game_over()

    
  #when snake touches food
  if head.distance(food) < 15:
    x = randint(-290,290)
    y = randint(-290,290)
    food.goto(x,y)

    #Create new segment and increment score 
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("green")
    new_segment.penup()
    segments.append(new_segment)
    delay -= 0.001
    score += 10
    
    if score > high_score:
      high_score = score
      
    update_score(score,high_score)

  #add segments to the snake one by one from the end
  for i in range(len(segments)-1,0,-1):
    x = segments[i-1].xcor()
    y = segments[i-1].ycor()
    segments[i].goto(x,y)

  #Place head at the front
  if len(segments) >= 1:
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x,y)

  move()

    
  #collision with body
  for segment in segments:
    if segment.distance(head) < 20:
      time.sleep(1)
      head.goto(0,100)
      head.direction = "stop"
      food.goto(0,0)

      game_over()
    
 
  time.sleep(delay)

win.mainloop()
  
  
