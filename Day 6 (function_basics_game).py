##Day 7

print("hello")
num_char = len("Hello")
print(num_char)

def my_function():
    print("Hello")
    print("Bye")

my_function()

##def turn_right():
##    turn_left()
##    turn_left()
##    turn_left()
##turn_left()
##move()
##turn_right()
##move()
##turn_right()
##move()
##turn_right()
##move()

## reeborg robot moving jump Challenge

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    turn_left()
    turn_right()
    move()
    turn_left()
##jump()
##jump()
##jump()
##jump()
##jump()
##jump()

for step in range(6):
    jump()


#usiing while loop
number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)

#2nd case
while not at_goal():
    jump()

#code challenge -lesson 62
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()


#Reboorg Code challwnge - 3rd
def turn_right():
    turn_left()
    turn_left()
    turn_left()

    
def jump():
    turn_left()
    if wall_in_front():
        turn_left()
        move()
    elif not wall_in_front():
        move()
    elif not wall_on_right():
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
    else:
        while wall_in_front()  != True:
            move()

while not at_goal():
    if front_is_clear() and not wall_on_right():
        turn_right()
        move()
    elif right_is_clear():
        turn_right()
        move()
    elif wall_in_front():
        jump()
    else:
        move()
    
#Final challenge
def turn_right():
    turn_left()
    turn_left()
    turn_left()

    
def jump():
    turn_left()
    if wall_in_front():
        turn_left()
        move()
    elif not wall_in_front():
        move()
    elif not wall_on_right():
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
    else:
        while wall_in_front()  != True:
            move()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear() and not wall_on_right():
        turn_right()
        move()

    elif wall_in_front():
        jump()
    else:
        move()
    

    
