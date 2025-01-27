import turtle as t
from time import sleep

from maze import maze, maze_states
from learning import QLearning

episode = 1
moves = 0

episodes = []

bob_px = 1
bob_py = 1

t.tracer(0, 0)

def get_state_num(px, py):
    for i in range(len(maze_states)):
        if maze_states[i] == (px, py):
            return i

def reset():
    global bob_px
    global bob_py

    global episode
    global moves
    global episodes

    print(f"Episode {episode}: {moves}{'+' if moves >= 200 else ''} moves {' (optimal # of moves!)' if moves == 18 else ''}")

    if episode == 100:
        print(episodes)
        quit()

    bob_px = 1
    bob_py = 1

    episodes.append(moves)

    episode += 1
    moves = 0

    safe_goto(bob, -175, 175, False)

def navigate(action):
    global bob_px
    global bob_py

    old_state_num = get_state_num(bob_px, bob_py)

    reward = -1
    if action == 0:
        if maze[bob_py][bob_px + 1] == 1:
            reward = -3
        else:
            bob.setheading(0)
            bob.forward(50)

            t.update()

            bob_px += 1

            if maze[bob_py][bob_px] == 3:
                reward = 1
                reset()
                sleep(1)
    elif action == 1:
        if maze[bob_py - 1][bob_px] == 1:
            reward = -3
        else:
            bob.setheading(90)
            bob.forward(50)

            t.update()

            bob_py -= 1

            if maze[bob_py][bob_px] == 3:
                reward = 1
                reset()
                sleep(1)
    elif action == 2:
        if maze[bob_py][bob_px - 1] == 1:
            reward = -3
        else:
            bob.setheading(180)
            bob.forward(50)

            t.update()

            bob_px -= 1

            if maze[bob_py][bob_px] == 3:
                reward = 1
                reset()
                sleep(1)
    elif action == 3:
        if maze[bob_py + 1][bob_px] == 1:
            reward = -3
        else:
            bob.setheading(270)
            bob.forward(50)

            t.update()

            bob_py += 1

            if maze[bob_py][bob_px] == 3:
                reward = 1
                reset()
                sleep(1)

    state_num = get_state_num(bob_px, bob_py)

    algorithm.update(old_state_num, action, reward, state_num)

def safe_goto(turtle, x, y, pendown = True):
    turtle.penup()
    turtle.goto(x, y)

    if pendown:
        turtle.pendown()

def square(turtle, size, pendown = True):
    turtle.pendown()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)

    turtle.end_fill()

    if not pendown:
        turtle.penup()

c = t.Turtle()
c.hideturtle()
c.speed(10000)
c.penup()

c_x = -250
c_y = 250

c.goto(c_x, c_y)

for row in maze:
    c_x = -250
    for point in row:
        safe_goto(c, c_x, c_y, False)

        if point == 1:
            square(c, 50, False)
        elif point == 2:
            c.color("#00bf63")
            square(c, 50, False)
            c.color("#000000")
        elif point == 3:
            c.color("#ffde59")
            square(c, 50, False)
            c.color("#000000")

        c_x += 50

    c_y -= 50

bob = t.Turtle()
safe_goto(bob, -175, 175, False)

t.update()

algorithm = QLearning(shape=(len(maze_states), 4))\

while True:
    moves += 1
    navigate(algorithm.get_action(get_state_num(bob_px, bob_py)))
    sleep(0.01)

    if moves == 200:
        reset()
        sleep(1)