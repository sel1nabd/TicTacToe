import pygame

pygame.init() # initialise all imported pygame modules

# Screen

screenWidth, screenHeight = 600, 600

rows, columns = 3, 3

cellSize = screenWidth // 3 # portioning off since it's a 3x3 grid

screen = pygame.display.set_mode((screenWidth, screenHeight)) # sets up actual screen window
pygame.display.set_caption("Tic Tac Toe") # name of the screen window

# Colours

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0) # crosses
blue = (0, 0, 255) # noughts

# Board state

board = [[None, None, None],
         [None, None, None],
         [None, None, None]] # this is a 2D List

current_player = "X" # Starting with X

running = True # main game loop


def draw_grid():

    # 2 grid vertical lines
    pygame.draw.line(screen, black, (cellSize, 0), (cellSize, screenHeight), 5) # first grid line
    pygame.draw.line(screen, black, (2 * cellSize, 0), (2 * cellSize, screenHeight), 5) # second grid line

    # 2 grid horizontal lines
    pygame.draw.line(screen, black, (0, cellSize), (screenWidth, cellSize), 5)
    pygame.draw.line(screen, black, (0, 2 * cellSize), (screenWidth, 2 * cellSize), 5)


def draw_xo():
    for row in range(rows): # row is a local variable !
        for col in range(columns):
            mark = board[row][col]
            if mark == "X":

                # Draw an X

                start_pos1 = (col * cellSize + 40, # x coord of the top left
                              row * cellSize + 40) # y coord of the top left
                end_pos1 = (col * cellSize + cellSize - 40, # x coord of the bottom right
                            row * cellSize + cellSize - 40) # y coord of the bottom right

                pygame.draw.line(screen, red, start_pos1, end_pos1, 10)

                start_pos2 = (col * cellSize + 40, row * cellSize + cellSize - 40)
                end_pos2 = (col * cellSize + cellSize - 40, row * cellSize + 40)
                pygame.draw.line(screen, red, start_pos2, end_pos2, 10)

            elif mark == "O":

                # Draw an O

                center_x = col * cellSize + cellSize // 2
                center_y = row * cellSize + cellSize // 2
                pygame.draw.circle(screen, blue, (center_x, center_y), 60, 10)


def check_winner():
    # Check row wins
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] != None:
            return board[r][0]

    # Check column wins
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] != None:
            return board[0][c]

    # Check diagonal wins
    if board[0][0] == board[1][1] == board[2][2] != None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != None:
        return board[0][2]

    return None  # No winner yet

def is_board_full(board):
    for row in board:
        for column in row:
            if column is None:
                return False
    return True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row = y // cellSize
            col = x // cellSize

            if board[row][col] is None:
                board[row][col] = current_player
                winner = check_winner()
                if winner:
                    print(f"{winner} wins!")
                    running = False
                else:
                    if is_board_full(board):
                        print("It's a Draw")
                        running = False
                    else:
                        # Switch player
                        current_player = "O" if current_player == "X" else "X"


    screen.fill(white)
    draw_grid()
    draw_xo()
    pygame.display.update()

pygame.quit()
