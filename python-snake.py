import turtle
import time
from random import randint

delay = 0.1
score = 0
high_score = 0

win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("blue")
win.setup(width=600,height=600)
win.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
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
update_score = turtle.Turtle()
update_score.speed(0)
update_score.color("white")
update_score.penup()
update_score.shape("square")
update_score.hideturtle()
update_score.goto(0,250)
update_score.write(f"Score {score}  High Score: {high_score}",align = "center",font=("arial",24,"bold"))

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

    #hide segments
    for segment in segments:
      segment.goto(100000,100000)
    #clear segments
    segments.clear()
    score = 0
    update_score.clear()
    update_score.write(f"Score: {score} High Score: {high_score}",align="center",font=("arial",24,"bold"))

    
  #when snake touches food
  if head.distance(food) < 15:
    x = randint(-290,290)
    y = randint(-290,290)
    food.goto(x,y)

    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("white")
    new_segment.penup()
    segments.append(new_segment)
    delay -= 0.001
    score += 10
    
    if score > high_score:
      high_score = score
      update_score.clear()
      update_score.goto(0,250)
      update_score.write(f"Score {score}  High Score: {high_score}",align = "center",font=("arial",24,"bold"))
  
  for i in range(len(segments)-1,0,-1):
    x = segments[i-1].xcor()
    y = segments[i-1].ycor()
    segments[i].goto(x,y)

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

      for segment in segments:
        segment.goto(1000,1000)
      segments.clear()
      score = 0
      update_score.clear()
      update_score.write(f"Score: {score} High Score: {high_score}",align="center",font=("arial",24,"bold"))
    
 
  time.sleep(delay)

win.mainloop()
  
  
