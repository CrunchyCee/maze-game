##########idea: text maze
#generate maze out of | , + , and -
#player character is a smiley?
#text input to move and reprint maze (rework later)
##########

#TODO Implement maze generator (user inputs maze size)
#TODO Implement GUI (tkinter?)
#TODO Implement keyboard events so user doesn't have to press enter each return
#Maybe try to make this again in pygame once complete

#create maze/player/other fields
maze_dim = 10
if maze_dim % 2 == 0:
    even = True
else:
    even = False
col_width = 2
row_width = 4*maze_dim + 2
vert_jump = row_width*2
horz_jump = col_width*2

def position(row, column):
    return ((4*maze_dim + 2)*row + 1) + 2*column

maze_template = """
+---+---+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+---+---+
"""

maze_test = """
+---+---+---+---+---+   +---+---+---+---+
|       |           |           |       |
+   +---+   +---+---+---+---+   +---+   +
|                                       |
+---+---+   +---+---+---+   +---+---+---+
|       |   |               |           |
+   +   +---+   +---+---+---+---+---+   +
|   |           |       |       |       |
+   +---+---+---+---+   +   +   +   +---+
|   |               |       |       |   |
+   +---+---+   +   +---+---+---+   +   +
|           |   |               |   |   |
+---+---+   +   +---+---+---+   +   +   +
|       |       |           |   |   |   |
+   +---+---+---+   +---+   +   +   +   +
|       |           |       |       |   |
+   +   +   +---+---+   +---+   +   +   +
|   |       |                   |       |
+---+---+   +---+---+---+---+   +---+   +
|                   |           |       |
+---+---+---+---+   +---+---+---+---+---+
"""

player = "☺"

#testing box
#print(maze_test[819])

#add player to starting pos
if even:
    pos = position(2*maze_dim - 1, maze_dim - 1)
else:
    pos = position(2*maze_dim - 1, maze_dim)
print(maze_test[:pos] + player + maze_test[pos + 1:])

#run game
running = True
win = False
while running:
    #request input direction
    direction = input("Type W, A, S, or D to move.\n")
    #change position based on input, cannot move past walls
    if (direction == "W") or (direction == "w"):
        if maze_test[pos - row_width] != "-":
           pos -= vert_jump
           #win condition (move across exit)
           if pos < position(0,0):
               pos += vert_jump
               win = True
               running = False
    elif (direction == "A") or (direction == "a"):
        if maze_test[pos - col_width] != "|":
            pos -= horz_jump
    elif (direction == "S") or (direction == "s"):
        if maze_test[pos + row_width] != "-":
            pos += vert_jump
            #invalid move (move across entrance)
            if pos > position(20,20):
                pos -= vert_jump
    elif (direction == "D") or (direction == "d"):
        if maze_test[pos + col_width] != "|":
            pos += horz_jump

    #print maze after each movement
    print(maze_test[:pos] + player + maze_test[pos + 1:])
    #print win statment
    if win:
        print("You win!")
