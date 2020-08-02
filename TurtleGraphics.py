import turtle 
import random 

def check():
    if player_one.pos() >= (300,100):
        print("player one wins !!")
        return True
    elif player_two.pos() <= (-300,-100):
        print("player two wins !!")
        return True
    return False
    
player_one = turtle.Turtle()
player_one.color("red")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200,100)
player_two = player_one.clone()
player_one.speed(1)
player_two.speed(1)
player_two.color("blue")
player_two.penup()
player_two.goto(-200,-100)
player_one.goto(300,60)
player_one.pendown()
player_one.begin_fill()
player_one.color("green")
player_one.circle(40)
player_one.end_fill()
player_one.color("red")
player_one.penup()
player_one.goto(-200,100)
player_two.goto(300,-140)
player_two.pendown()
player_two.color("green")
player_two.begin_fill()
player_two.circle(40)
player_two.end_fill()
player_two.color("blue")
player_two.penup()
player_two.goto(-200,-100)
die = [1,2,3,4,5,6]
while True:
    player_one_turn = input("Player One turn\nPress enter to roll the die : ")
    die_result = random.choice(die)
    print("The die result is : "+str(die_result))
    print("The number of steps the die get move is "+str(20*die_result))
    player_one.forward(20*die_result)
    if(check()):
        break
    player_two_turn = input("Player Two turn\nPress enter to roll the die : ")
    die_result = random.choice(die)
    print("The die result is : "+str(die_result))
    print("The number of steps the die get move is "+str(20*die_result))
    player_two.forward(20*die_result)
    if(check()):
        break
