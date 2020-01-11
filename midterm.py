import turtle
import os
import time

my_turt = turtle.Turtle()
screen = turtle.Screen()
t = turtle.Pen()
screen.setup(width = 1.0, height = 1.0)
my_turt.hideturtle()


myPen = turtle.Turtle()
myPen.speed(1)
myPen.color("#000088")
myPen.pensize(10)



def intro():
   screen.bgcolor('grey')

   my_turt.write('''
   ***********************
 
   *   Midterm Project  *              
   * Crystal Robertson  *
   * Musca Constellation*
   *        v1.0              *
   *                          *
   ***********************
   ''', align="center",font=("Arial", 10, "bold")
   )
   time.sleep(5)
   




def slide3():
   screen.bgpic('musca-.png')
   screen.reset()
   my_turt.hideturtle()
   time.sleep(5)


   




def drawConstellation(constellation):
  myPen.color("white")
  screen.bgcolor('white')
  myPen.pensize(10)  
  myPen.goto(constellation[0])
  myPen.begin_fill()  
  myPen.circle(2)
  myPen.end_fill()
  myPen.pendown()
  for star in constellation:
    myPen.goto(star)
    myPen.begin_fill()  
    myPen.circle(2)
    myPen.end_fill()
  myPen.penup()
  myPen.goto(-174,152)
  screen.reset()
  time.sleep(5)




yclick = 0
def getcoordinates():
    turtle.onscreenclick(modifyglobalvariables)
def modifyglobalvariables(rawx,rawy):
    global xclick
    global yclick
    xclick = int(rawx//1)
    yclick = int(rawy//1)
    print("[",xclick,"," ,yclick, "]" ,sep="")
getcoordinates()



    



def drawConstellation2(constellation):
  myPen.color('white')
  myPen.pensize(3)
  screen.bgpic('bright.png')
  myPen.goto(constellation[0])
  myPen.begin_fill()  
  myPen.circle(2)
  myPen.end_fill()
  myPen.pendown()
  for star in constellation:
    myPen.goto(star)
    myPen.write('NGC 4833',font=("Arial", 8, "normal"))
    myPen.begin_fill()  
    myPen.circle(2)
    myPen.end_fill()
  myPen.penup()
  myPen.goto(-197,159)
  time.sleep(5)
  


musca = [[-174,152],[-219,43],[-123,30],[-150,139],[-174,152],[-150,139],[-51,176],[120,179]]
musca2 = [[-197,159],[-125,104],[-198,162],[-283,-104],[-110,-138],[-131,98],[-1,174],[238,229]]
def main():
 intro()
 slide3()
 myPen.penup()
 myPen.goto(-174,152)
 drawConstellation(musca)
 myPen.goto(-197,159)
 drawConstellation2(musca2)

main()
