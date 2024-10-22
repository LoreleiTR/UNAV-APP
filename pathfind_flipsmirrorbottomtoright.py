import pygame
import math
from queue import PriorityQueue
import cv2
import numpy as np



# Pygame window setup
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path Finding Techno")




# Define colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# Spot class for grid





class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = ORANGE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():  # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():  # UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():  # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():  # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False

# Heuristic function for A* (Manhattan distance)
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

# Reconstruct the path
def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()

# A* algorithm
def algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False

# Process image and create grid based on colors
def process_image_to_grid(image_path, rows):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (rows, rows))
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    pink_lower = np.array([150, 0, 150])
    pink_upper = np.array([255, 150, 255])
    green_lower = np.array([0, 100, 0])
    green_upper = np.array([100, 255, 100])

    grid = [[0 for _ in range(rows)] for _ in range(rows)]

    for i in range(rows):
        for j in range(rows):
            pixel = image_rgb[i, j]
            if (pink_lower <= pixel).all() and (pixel <= pink_upper).all():
                grid[i][j] = 1  # Wall
            elif (green_lower <= pixel).all() and (pixel <= green_upper).all():
                grid[i][j] = 0  # Path

    return grid

# Create grid with walls and paths
def make_grid_from_image(rows, width, image_grid):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            if image_grid[i][j] == 1:
                spot.make_barrier()  # Mark as barrier if it's a wall
            grid[i].append(spot)
    return grid

# Draw grid lines
def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

# Draw the window
def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()

# Get clicked position
def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col

# Main function to run the program
def main(win, width):
    ROWS = 50
    image_grid = process_image_to_grid('your_image.png', ROWS)
    grid = make_grid_from_image(ROWS, width, image_grid)

    start = None
    end = None

    run = True
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]: # LEFT CLICK
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start and spot != end and not spot.is_barrier():
                    start = spot
                    start.make_start()

                elif not end and spot != start and not spot.is_barrier():
                    end = spot
                    end.make_end()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)

                    algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid_from_image(ROWS, width, image_grid)

    pygame.quit()

def process_image_to_grid(image_path, rows):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image not found at path: {image_path}")
    
    image = cv2.resize(image, (rows, rows))
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    pink_lower = np.array([150, 0, 150])
    pink_upper = np.array([255, 150, 255])
    green_lower = np.array([0, 100, 0])
    green_upper = np.array([100, 255, 100])

    grid = [[0 for _ in range(rows)] for _ in range(rows)]

    for i in range(rows):
        for j in range(rows):
            pixel = image_rgb[i, j]
            if (pink_lower <= pixel).all() and (pixel <= pink_upper).all():
                grid[i][j] = 1  # Wall
            elif (green_lower <= pixel).all() and (pixel <= green_upper).all():
                grid[i][j] = 0  # Path

    return grid


def main(win, width):
    ROWS = 50  # Define ROWS here
    image_grid = process_image_to_grid('C:\\Users\\Lorelei\\Downloads\\deg3.png', ROWS)
    grid = make_grid_from_image(ROWS, width, image_grid)

    start = None
    end = None

    run = True
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  # LEFT CLICK
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start and spot != end and not spot.is_barrier():
                    start = spot
                    start.make_start()

                elif not end and spot != start and not spot.is_barrier():
                    end = spot
                    end.make_end()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)

                    algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid_from_image(ROWS, width, image_grid)

    pygame.quit()

    image_grid = process_image_to_grid('map/map.png', ROWS)

# Run the main function

main(WIN, WIDTH)

