import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
WIDTH, HEIGHT = 540, 600
FPS = 60

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Example Sudoku board
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# Define the grid and cell size
grid = [row[:] for row in board]  # Create a copy of the original board
cell_size = WIDTH // 9

# Function to draw the Sudoku grid
def draw_grid():
    for i in range(1, 9):
        if i % 3 == 0:
            pygame.draw.line(screen, BLACK, (0, i * cell_size), (WIDTH, i * cell_size), 2)
            pygame.draw.line(screen, BLACK, (i * cell_size, 0), (i * cell_size, HEIGHT), 2)
        else:
            pygame.draw.line(screen, BLACK, (0, i * cell_size), (WIDTH, i * cell_size), 1)
            pygame.draw.line(screen, BLACK, (i * cell_size, 0), (i * cell_size, HEIGHT), 1)

# Function to draw the numbers on the grid
def draw_numbers():
    font = pygame.font.SysFont("calibri", 40)

    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                text = font.render(str(board[i][j]), True, BLACK)
                x = j * cell_size + (cell_size - text.get_width()) // 2
                y = i * cell_size + (cell_size - text.get_height()) // 2
                screen.blit(text, (x, y))

# Function to get the clicked cell
def get_clicked_cell(pos):
    row = pos[1] // cell_size
    col = pos[0] // cell_size
    return row, col

# Function to check if a number is valid for a given cell
def is_valid_number(num, row, col):
    # Check row
    if num in board[row]:
        return False

    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check box
    box_start_row, box_start_col = 3 * (row // 3), 3 * (col // 3)
    if num in [board[i][j] for i in range(box_start_row, box_start_row + 3) for j in range(box_start_col, box_start_col + 3)]:
        return False

    return True

# Function to clear the cell
def clear_cell(row, col):
    board[row][col] = 0

# Main game loop
running = True
selected_cell = None
stack = []

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            selected_cell = get_clicked_cell(pos)

    keys = pygame.key.get_pressed()
    if selected_cell is not None:
        for key in range(pygame.K_1, pygame.K_9 + 1):
            if keys[key]:
                row, col = selected_cell
                num = int(pygame.key.name(key))
                if is_valid_number(num, row, col):
                    board[row][col] = num
                    stack.append((row, col))
                else:
                    # If the number is not valid, clear the cell and backtrack
                    clear_cell(row, col)
                    if stack:
                        row, col = stack.pop()
                        selected_cell = (row, col)

    draw_grid()
    draw_numbers()

    pygame.display.flip()
    clock.tick(FPS)

# Display the initial state
print("Initial State:")
for row in board:
    print(row)

# Perform the solving algorithm (backtracking)
# ... (you can include your solving algorithm here)

# Display the final state
print("\nFinal State:")
for row in board:
    print(row)

pygame.quit()
sys.exit()
