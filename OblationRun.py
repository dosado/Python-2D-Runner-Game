# FINAL OUTPUT IN CMSC 11  for the 1st Semester of SY 2019-2020
# Under the instruction of Ms. Christi Calina Cala-or
# Created by BS in Compuer Science 1 students:
# 	Bernales, Hadjie Jr.
# 	Dela Cruz, Sophe Mae
#	Dosado, Michael Vincent
#	Vedasto, Gorge Lichael Vann
#
#UNIVERSITY OF THE PHILIPPINES VISAYAS


# Import modules
import turtle
import random
import math
import pygame

start = False #the game is false until the player has not pressed the 'Space' buttom to start the game
game = True #game is always true bcs if its value becomes 'false', the window closes because main function cannot execute
gameover= False #gameover is False until player crashes to barriers

# Setting up Background music
pygame.init()     # Initialize pygame for background music.
pygame.mixer.Channel(0).play(pygame.mixer.Sound("8bitUP.wav"), -1) # -1 means To play infinitely throughout the program

# Registering Shapes
turtle.register_shape("char.gif")
turtle.register_shape("sablay1.gif")
turtle.register_shape("bg1.gif")
turtle.register_shape("bg2.gif")
turtle.register_shape("bg3.gif")
turtle.register_shape("bluebook.gif")
turtle.register_shape("greenbook.gif")
turtle.register_shape("orangebook.gif")
turtle.register_shape("gameover.gif")
turtle.register_shape("title.gif")


# Setup Screen
wn = turtle.Screen()
wn.setup(width =1199, height=1040, startx =200, starty=0)    #It sets the dimensions of the window and its display position on the screen .
wn.bgpic("bg1.gif") 
wn.tracer(25)    # To accelerate animation of turtles


# Setup moving background 
#Background was set as turtles to enable animation
background1 = turtle.Turtle()    # Creating a turtle object.
background1.shape('bg1.gif')
background1.penup()              # In penup(), the turtle will move around the screen but it will not draw its pen state(trace).
background1.setposition(0, 0)    # The absolute position of the background to center (0,0).
background1.setheading(270)      # It sets the direction of the background to 270 degrees which is South.
background2 = turtle.Turtle()
background2.shape('bg2.gif')
background2.penup()
background2.setposition(0, 1030) #2nd BG is set in the position right after the 1st BG
background2.setheading(270)
background3 = turtle.Turtle()
background3.shape('bg3.gif')
background3.penup()
background3.setposition(0, 2060) #3rd BG is set in the position right after the 2nd BG
background3.setheading(270)

# Create player turtle
player = turtle.Turtle()
player.shape("char.gif")
player.hideturtle() 
player.speed(0) #to animate player instantly
player.penup()
player.setposition(0, -250) # position set on the lower level of screen
player.setheading(90) #player faces upwards
player.showturtle()


# Creating barriers
barriers = []
barrierlist = ["sablay1.gif", "bluebook.gif", "bluebook.gif", "orangebook.gif", "greenbook.gif"]

def initbarrier(): # barriers' initial position
	for i in range(9):  
		barriers.append(turtle.Turtle()) # 9 turtles were appended to the list as barriers
		(barriers[i]).hideturtle()    # To hide the barriers 
	for barrier in barriers:
		barrier.penup()     # No trace of each barrier
		barrier.speed(0)    # To move the barriers instantly
		barrier.shape(random.choice(barrierlist))     # Each barrier will be randomly set based from the list 'barrierlist'.
		barrier.setheading(270) #barriers are set downwards, facing the direction of player
	ycors = [750, 1000, 1250, 1500, 1750, 2000, 2250]    # Coordinates for the barriers
	ycor01 = random.choice(ycors)    # The coordinates or positions of the barriers will be randomly chosen.
	ycors.remove(ycor01)     # To avoid the repetition of occurence of each barriers.
	# Barriers' initial position 
	barriers[0].setposition(-175, ycor01)
	barriers[1].setposition(0, ycor01)
	ycor23 = random.choice(ycors)
	ycors.remove(ycor23)
	barriers[2].setposition(-175, ycor23)
	barriers[3].setposition(175, ycor23)
	ycor45 = random.choice(ycors)
	ycors.remove(ycor45)
	barriers[4].setposition(0, ycor45)
	barriers[5].setposition(175, ycor45)
	ycor06 = random.choice(ycors)
	ycors.remove(ycor06)
	barriers[6].setposition(random.randrange(-175, 176, 350), ycor06)
	ycor07 = random.choice(ycors)
	ycors.remove(ycor07)
	barriers[7].setposition(random.randrange(0, 176, 175), ycor07)
	ycor08 = random.choice(ycors)
	ycors.remove(ycor08)
	barriers[8].setposition(random.randrange(-175, 1, 175), ycor08)
	for barrier in barriers:
		barrier.showturtle()    # To make the Turtle visible.


initbarrier()

speed = 3
def move():
	for barrier in barriers:
		barrier.forward(speed)    # The speed of each barriers is 3.


def removebarier(): # To remove the barriers after they are offscreen
	for barrier in barriers:
		if barrier.ycor() <= -450:
			barriers.remove(barrier)
			barrier.hideturtle()


def returnbarrier():    # To create the barriers again after the previous pass
	if len(barriers) == 0:
		global speed
		speed += 0.3 #speed is incremented in every new wave of barriers
		initbarrier() #creates new barriers


score = 0

# Collisions of player to barriers
def collision():
	global start, score, gameover, mypen, game
	for barrier in barriers:   # Barrier collision
		barrierdistance = math.sqrt(math.pow(player.xcor() - barrier.xcor(), 2) + math.pow(player.ycor() - barrier.ycor(), 2)) #distance formula was used to determine if the player has hit a barrier
		if barrier.shape() == "bluebook.gif" or barrier.shape() == "greenbook.gif" or barrier.shape() == "orangebook.gif":
			if barrierdistance < 79:
				start = False     # The barriers will stop to move if the character collided with it, and animation will cease
				mypen.hideturtle()
				mypen.setposition(0, 150) #score is hidden and repositioned
				mypen.write(score, align='center', font=('Impact', '100', 'normal'))    # It will display the final score and the font size will be bigger for emphasis.
				gameover = True    # it will display the game over sigh 
								
				
		if barrier.shape() == "sablay1.gif":
			if barrierdistance < 45:
				barrier.hideturtle() #the sablay will disappear
				barriers.remove(barrier) #sablay will be removed from the list of barriers

				# draw score on screen
				score += 1 #when layer gets a sablay, score is incremented by 1
				#sfx for getting sablay
				pygame.init()
				pygame.mixer.Channel(1).play(pygame.mixer.Sound("8bitcoin.wav"))
				pygame.mixer.Channel(1).set_volume(1)
				mypen.clear()
				mypen.write(score,  align='center', font=('Impact', '50', 'normal')) #updates score every time player gets a sablay
				mypen.clear() 
				


# Define key functions
def turnLeft():    
	if player.xcor() == -175:    # It will not do anything, it cannot go left anymore since player is already in the left most position
		pass
	elif player.xcor() == 0: #move left from middle lane 
		player.setposition(-175, -250)
	elif player.xcor() == 175: #move left from right most lane
		player.setposition(0, -250)
	   

def turnRight():   
	if player.xcor() == 175:    # The character will remain if it is on the right most side already.
		pass
	elif player.xcor() == 0: #move right from middle lane
		player.setposition(175, -250)
	elif player.xcor() == -175: #move right from left most lane
		player.setposition(0, -250)

def space():    # The space function will start the game.
	global start
	title.hideturtle() #it will hide the title 'oblation run'
	start = True 
   
# Set keyboard binding
def keys():
	turtle.listen()    # The turtle will listen on the two keys.
	turtle.onkey(turnLeft, "Left") #when 'left key' is pressed, turnLeft function is executed
	turtle.onkey(turnRight, "Right")  #when right key' is pressed, turnRight function is executed


def deactivate_keys(): # deactivates control keys (applied before the game, and when gameover)
    turtle.listen()
    turtle.onkey(None, "Left")
    turtle.onkey(None, "Right")



mypen = turtle.Turtle() #turtle for score

def showscore():   # The score will display.
	mypen.color('yellow')
	mypen.penup()
	mypen.speed(0)
	mypen.setposition(0, 300) #position is set on the upper level of screen 
	mypen.write(score,  align='center', font=('Impact', '50', 'normal')) #mypen will display the value of the variable 'score'
	mypen.undo()    # For each score increase, the previous score will be invisible to show the new score clearly.


#Creating turtles that displays the instructions before game begins
mypen1 = turtle.Turtle() #'Press space to start'
mypen2 = turtle.Turtle() #'Use the left & right arrows. Avoid getting singko.And get those sablays. '

def instructions():    #displays  Instructions before the start of the game
	mypen1.color('red')
	mypen1.penup()
	mypen1.hideturtle()
	mypen1.setposition(0, -50)
	mypen1.write('PRESS SPACE TO START', align='center', font=('Pixelated', '45', 'normal'))
	mypen1.undo()
	mypen2.penup()
	mypen2.hideturtle()
	mypen2.setposition(0, -200)
	mypen2.write('Use the left & right arrows.\n       Avoid getting singko. \n     And get those sablays.', align='center', font=('Game Over', '50', 'normal'))


# Title of the game (OblationRun)
title = turtle.Turtle()    
title.shape('title.gif')
title.hideturtle()
title.speed(0)
title.penup()
title.setposition(0, 200)


########## THE GAME PROPER########
def main():   
	while game:
		if gameover == True:   # If the character collided with the obstacles, it will be game over.
			g_over = turtle.Turtle() # turtle that displays the gameover sign 
			g_over.penup()
			g_over.shape('gameover.gif')       
			mypen.showturtle() #shows the final score just above the gameover sign
			deactivate_keys() #the character should not move between lines when gameover
						
		else:
			title.showturtle()    # Title display
			instructions()        # Instructions display
			turtle.listen()
			turtle.onkey(space, "space") #space must be presses to start game

			while start:     # If the player presses the Space button, the game will start and the barriers will start to come down.
				
				keys() #enables the control keys(left and right)

				#hides the instructions
				mypen1.hideturtle()   
				mypen1.clear()
				mypen2.clear()
				mypen2.hideturtle()

				#the background will start to move downward (illusion to make it seem the player is moving)
				background1.forward(2)
				background2.forward(2)
				background3.forward(2)

				#looping the motion of  backgrounds
				if background1.ycor() < -1030:
					background1.hideturtle()
					background1.setposition(0, 2060)
					background1.showturtle()
				if background2.ycor() < -1030:
					background2.hideturtle()
					background2.setposition(0, 2060)
					background2.showturtle()
				if background3.ycor() < -1030:
					background3.hideturtle()
					background3.setposition(0, 2060)
					background3.showturtle()
				move() # barriers will move downwards
				collision() #checks if player crashes with barriers or sablay
				showscore() #shows the current score
				removebarier() #removes barrier if it gets out of screen
				returnbarrier() #creates next wave of  barriers


main() # calls the main function 

