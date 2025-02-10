import turtle as t
from time import sleep
from maze import maze, maze_states
from learning import QLearning

# Initialize global variables
episode = 1
moves = 0
episodes = []
bob_px, bob_py = 1, 1  # Bob's initial position
t.tracer(0, 0)  # Disable turtle animation for performance

reload_rate = 0.005

def get_state_num(px, py):
    """Get the index of the state given Bob's coordinates."""
    for i, state in enumerate(maze_states):
        if state == (px, py):
            return i

def reset():
    """Reset the game for a new episode."""
    global bob_px, bob_py, episode, moves, episodes

    print(f"Episode {episode}: {moves}{'+' if moves >= 200 else ''} moves {' (optimal # of moves!)' if moves == 18 else ''}")

    if episode == 100:
        print(episodes)
        quit()

    bob_px, bob_py = 1, 1  # Reset Bob's position
    episodes.append(moves)
    episode += 1
    moves = 0

    safe_goto(bob, -175, 175, False)

def navigate(action):
    """Navigate Bob based on the action taken."""
    global bob_px, bob_py
    global moves

    old_state_num = get_state_num(bob_px, bob_py)
    reward = -1  # Default reward for each move

    # Define movement directions
    directions = {
        0: (1, 0, 0),    # Right
        1: (0, -1, 90),  # Up
        2: (-1, 0, 180), # Left
        3: (0, 1, 270)   # Down
    }

    dx, dy, heading = directions[action]
    adj_state = get_adjacent_state(dx, dy)

    if adj_state is not None:
        moves += adj_state

        bob.setheading(heading)
        for i in range(adj_state):
            bob.forward(50)
            t.update()
            sleep(reload_rate)

        bob_px += dx * adj_state
        bob_py += dy * adj_state

        # Check if Bob reached the goal
        if maze[bob_py][bob_px] == 4:
            reward = 1
            reset()
            sleep(1)
    else:
        moves += 1
        reward = -3  # Penalize for hitting a wall

    state_num = get_state_num(bob_px, bob_py)
    algorithm.update(old_state_num, action, reward, state_num)

def get_adjacent_state(dx, dy):
    """Get the number of steps Bob can take in the specified direction."""
    limit = 11
    for i in range(1, limit - 1):
        adj_block = maze[bob_py + dy * i][bob_px + dx * i]
        if adj_block in (2, 3, 4):
            return i  # Return the distance to the next valid block
        elif adj_block == 1:
            break  # Stop if a wall is hit
    return None  # No valid movement

def safe_goto(turtle, x, y, pendown=True):
    """Move the turtle safely to the specified coordinates."""
    turtle.penup()
    turtle.goto(x, y)
    if pendown:
        turtle.pendown()

def draw_square(turtle, size, pendown=True):
    """Draw a filled square with the specified size."""
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()
    if not pendown:
        turtle.penup()

# Initialize turtle for drawing the maze
c = t.Turtle()
c.hideturtle()
c.speed(0)  # Fastest drawing speed
c.penup()

# Draw the maze
for y, row in enumerate(maze):
    for x, point in enumerate(row):
        safe_goto(c, -250 + x * 50, 250 - y * 50, False)
        if point == 1:
            draw_square(c, 50, False)
        elif point == 3:
            c.color("#00bf63")
            draw_square(c, 50, False)
            c.color("#000000")
        elif point == 4:
            c.color("#ffde59")
            draw_square(c, 50, False)
            c.color("#000000")

# Initialize Bob's turtle
bob = t.Turtle()
safe_goto(bob, -175, 175, False)
t.update()

# Initialize Q-learning algorithm
algorithm = QLearning(shape=(len(maze_states), 4))

# Main loop for the maze
while True:
    action = algorithm.get_action(get_state_num(bob_px, bob_py))
    navigate(action)

    sleep(reload_rate)

    if moves == 200:
        reset()
        sleep(1)