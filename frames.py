import curses, time

import data

stdscr = curses.initscr()
curses.noecho()


def animate():
    for frame in data.frames:
        stdscr.addstr(0,0, frame, curses.A_NORMAL)
        time.sleep(0.1)
        stdscr.refresh()

def main():
    while(True):
        animate()


if __name__ == '__main__':
    main()
