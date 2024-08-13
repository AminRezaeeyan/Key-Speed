import curses
from records import record_manager
from text import text_generator


def show_menu(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, 'Key Speed', curses.color_pair(4))
    stdscr.addstr(3, 0, '1) Start Typing Test', curses.color_pair(5))
    stdscr.addstr(4, 0, '2) Records', curses.color_pair(5))
    stdscr.addstr(5, 0, '3) Exit', curses.color_pair(5))
    stdscr.addstr(7, 0, 'Enter your choice(1/2/3)', curses.color_pair(2))
    curses.curs_set(0)
    stdscr.refresh()

    choice = chr(stdscr.getch())
    while choice not in ['1', '2', '3']:
        stdscr.addstr(7, 0, 'Enter a valid choice(1/2/3)', curses.color_pair(3))
        stdscr.refresh()
        choice = chr(stdscr.getch())
    return choice


def show_records(stdscr):
    stdscr.clear()
    for index, record in enumerate(record_manager.read_records()):
        stdscr.addstr(index, 0, f'{record[0]:<6}{record[1]:<11}{record[2]:<21}{record[3]:<19}{record[4]:<7}',
                      curses.color_pair(4) if index == 0 else curses.color_pair(1))

    curses.curs_set(0)
    stdscr.refresh()
    stdscr.getch()


def get_text_source(stdscr):
    stdscr.clear()

    stdscr.addstr(0, 0, 'Key Speed', curses.color_pair(4))
    stdscr.addstr(3, 0, 'Choose Text Source:', curses.color_pair(4))
    stdscr.addstr(3, 0, '1) Type your own text', curses.color_pair(5))
    stdscr.addstr(4, 0, '2) Use a random text', curses.color_pair(5))
    stdscr.addstr(7, 0, 'Enter your choice(1/2)', curses.color_pair(2))
    curses.curs_set(0)
    stdscr.refresh()

    choice = chr(stdscr.getch())
    while choice not in ['1', '2']:
        stdscr.addstr(7, 0, 'Enter a valid choice(1/2)', curses.color_pair(3))
        stdscr.refresh()
        choice = chr(stdscr.getch())

    if choice == '2':
        return text_generator.generate_random_text()

    curses.echo()
    text = ''

    while len(text) < 20:
        stdscr.clear()
        stdscr.addstr(0, 0, "Enter a text between 20 and 200 characters",
                      curses.color_pair(4) if text == '' else curses.color_pair(3))
        text = stdscr.getstr(2, 0, 200).decode("utf-8").rstrip('\n')
        stdscr.refresh()

    curses.noecho()
    return text
