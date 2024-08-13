from curses import wrapper
import UI
from UI import menu, typing_test


def main(stdscr):
    UI.curses_init()

    while True:
        choice = (menu.show_menu(stdscr))

        match choice:
            case '1':
                target_text = menu.get_text_source(stdscr)
                typing_test.start(stdscr, target_text)
            case '2':
                menu.show_records(stdscr)
            case '3':
                break


if __name__ == '__main__':
    wrapper(main)
