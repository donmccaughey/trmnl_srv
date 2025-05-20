from .constants import HEIGHT, WIDTH
from .screen import Screen


def write_intro_screen():
    screen = Screen(WIDTH, HEIGHT, 64)

    line1 = 'Welcome to'
    line2 = 'trmnl_srv!'
    line_width = max(len(line1), len(line2))
    col = (screen.cols - line_width + 1) // 2
    row = (screen.rows - 2 + 1) // 2

    screen.write(col, row, line1)
    screen.write(col, row + 1, line2)

    return screen
