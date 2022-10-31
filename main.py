from utils.init import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Paint")


def initGrid(rows, columns, color):
    grid = []

    for row in range(rows):
        grid.append([])
        for column in range(columns):
            grid[row].append(color)

    return grid


def drawGrid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i *
                             PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(win, COLOR_BLACK, (0, i * PIXEL_SIZE),
                             (WIDTH, i * PIXEL_SIZE))

        for i in range(COLS + 1):
            pygame.draw.line(win, COLOR_BLACK, (i * PIXEL_SIZE, 0),
                             (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))


def draw(win, grid, buttons):
    win.fill(BACKGROUND_COLOR)
    drawGrid(win, grid)

    for button in buttons:
        button.draw(win)

    pygame.display.update()


def getRowAndColumnPosition(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError

    return row, col


if __name__ == "__main__":

    run = True
    clock = pygame.time.Clock()
    grid = initGrid(ROWS, COLS, BACKGROUND_COLOR)
    drawing_color = COLOR_BLACK

    button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25
    buttons = [
        Button(10, button_y, 50, 50, COLOR_BLUE),
        Button(70, button_y, 50, 50, COLOR_YELLOW),
        Button(130, button_y, 50, 50, COLOR_RED),
        Button(190, button_y, 50, 50, COLOR_GREEN),
        Button(250, button_y, 50, 50, COLOR_ORANGE),
        Button(310, button_y, 50, 50, COLOR_WHITE),
        Button(370, button_y, 50, 50, COLOR_BLACK),
        Button(430, button_y, 50, 50, COLOR_GRAY),
        Button(490, button_y, 50, 50, COLOR_WHITE, "Erase", COLOR_BLACK),
        Button(550, button_y, 50, 50, COLOR_WHITE, "Clear", COLOR_BLACK),
    ]

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()

                try:
                    row, col = getRowAndColumnPosition(pos)
                    grid[row][col] = drawing_color
                except IndexError:
                    for button in buttons:
                        if not button.clicked(pos):
                            continue

                        drawing_color = button.color
                        if button.text == "Clear":
                            grid = initGrid(ROWS, COLS, BACKGROUND_COLOR)
                            drawing_color = COLOR_BLACK

        draw(WIN, grid, buttons)
