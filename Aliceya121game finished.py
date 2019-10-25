# a121_catch_a_turtle.py
#-----import statements-----# 
import turtle as trtl
import random 


#-----game configuration----
turtleshape="arrow"
turtlesize= 3
turtlecolor="gold"

score= 0


timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False



#-----initialize turtle-----
deal= trtl.Turtle(shape=turtleshape)
deal.color(turtlecolor)
deal.shapesize(turtlesize)
deal.speed(230)
#scorewiter 

score_writer=trtl.Turtle()
score_writer.ht()
score_writer.penup()
score_writer.goto(-370,270)

font_setup=("Arial", 30, "bold")
score_writer.write(score, font=font_setup) 


counter =  trtl.Turtle()
counter.ht()
counter.penup()
counter.goto(300,275)



#-----game functions--------
def deal_clicked(x,y):
    change_position()
    update_score()
   

def change_position():
    print("deal got clicked") 
    deal.penup()
    deal.ht()
    if not timer_up:
        dealx = random.randint(-400,400)
        dealy = random.randint(-300,300)
        deal.goto(dealx,dealy)
        deal.st()
def update_score():
    global score
    score += 1
    print(score)
    score_writer.clear()
    score_writer.write(score, font=font_setup) 
230

def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("pulled a sneaky on you ", font=font_setup)
        timer_up = True
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval) 

  


#-----events----------------

wn = trtl.Screen()
wn.bgcolor("red")
wn.ontimer(countdown, counter_interval)
deal.onclick(deal_clicked) 
wn.mainloop()