import curses

def get_rows_and_start_pos():
    try:
        with open('day6.txt', 'r') as r:
            content = r.read()
    except FileNotFoundError:
        print("Error: 'day6.txt' file not found!")
        exit(1)

    rows = content.splitlines()
    rows = [list(row) for row in rows]
    i, j = 0, 0

    for y, row in enumerate(rows):
        for x, val in enumerate(row):
            if val == '^':
                i, j = x, y

    return [rows, i, j]

def next(dir):
    if dir == (0, -1):
        return (1, 0)
    elif dir == (1, 0):
        return (0, 1)
    elif dir == (0, 1):
        return (-1, 0)
    elif dir == (-1, 0):
        return (0, -1)
    else:
        return -1

def draw_menu(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    rows, x, y = get_rows_and_start_pos()
    seen = set()
    dir = (0, -1)

    # Viewport tracking
    viewport_x = 0
    viewport_y = 0

    while y >= 0 and y < len(rows) and x >= 0 and x < len(rows[y]):
        if (x, y) in seen and (x + next(dir)[0], y + next(dir)[1]) in seen:
            curses.delay_output(0)
        if rows[y + dir[1]][x + dir[0]] == '#':
            dir = next(dir)
        seen.add((x, y))
        rows[y][x] = 'X'
        x += dir[0]
        y += dir[1]
        viewport_x += dir[0]
        viewport_y += dir[1]

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        # Dimensions of the visible area
        visible_height = height - 2  # Reserve space for instructions
        visible_width = width

        # Adjust viewport
        viewport_x = max(0, min(viewport_x, max(len(row) for row in rows) - visible_width))
        viewport_y = max(0, min(viewport_y, len(rows) - visible_height))

        try:
            for idx, row in enumerate(rows[viewport_y:viewport_y + visible_height]):
                for col_idx, char in enumerate(row[viewport_x:viewport_x + visible_width]):
                    # Calculate absolute position of the character
                    abs_y = viewport_y + idx
                    abs_x = viewport_x + col_idx

                    # Highlight the character at rows[y][x]
                    if abs_y == y and abs_x == x:
                        stdscr.addch(idx, col_idx, "^", curses.color_pair(2))
                    else:
                        stdscr.addch(idx, col_idx, char, curses.color_pair(1))
        except curses.error:
            pass  # Ignore errors if the terminal is too small

        # Display instructions
        stdscr.addstr(height - 1, 0, "Use arrow keys to scroll. Press 'q' to quit.", curses.color_pair(1))

        # Refresh the screen
        stdscr.refresh()

        curses.delay_output(0)

        # Handle input
        # k = stdscr.getch()

        # if k == curses.KEY_UP and viewport_y > 0:
        #     viewport_y -= 1
        # elif k == curses.KEY_DOWN and viewport_y < len(rows) - visible_height:
        #     viewport_y += 1
        # elif k == curses.KEY_LEFT and viewport_x > 0:
        #     viewport_x -= 1
        # elif k == curses.KEY_RIGHT and viewport_x < max(len(row) for row in rows) - visible_width:
        #     viewport_x += 1

    # Wait for 'q' to quit
    while k != ord('q'):
        k = stdscr.getch()

def main():
    curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()
