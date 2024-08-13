import curses
import time
import datetime
from records import record_manager


def start(stdscr, target_text):
    stdscr.clear()
    stdscr.addstr(0, 0, 'Press any key to start typing! Get ready...', curses.color_pair(4))
    stdscr.refresh()
    stdscr.getch()
    type_test(stdscr, target_text, time.time())


def type_test(stdscr, target_text, start_time):
    typing_accuracy_stack = []
    cursor_index = 0

    stdscr.clear()
    stdscr.addstr(0, 0, target_text, curses.color_pair(1))
    stdscr.refresh()

    while cursor_index < len(target_text):
        key = chr(stdscr.getch())

        if ord(key) in [curses.KEY_EXIT, 27]:
            exit(0)
        elif key in [chr(curses.KEY_BACKSPACE), '\b', 'x7f']:
            if cursor_index == 0:
                continue

            typing_accuracy_stack.pop()
            cursor_index -= 1
            stdscr.addstr(0, cursor_index, target_text[cursor_index], curses.color_pair(1))
        else:
            typed_correct = (key == target_text[cursor_index])
            typing_accuracy_stack.append(typed_correct)

            color_pair = curses.color_pair(2) if typed_correct else curses.color_pair(3)
            char = '_' if (target_text[cursor_index] == ' ' and not typed_correct) else target_text[cursor_index]

            stdscr.addstr(0, cursor_index, char, color_pair)
            cursor_index += 1

    correct_chars = typing_accuracy_stack.count(True)
    wrong_chars = len(target_text) - correct_chars
    time_elapsed = time.time() - start_time
    wpm = calculate_wpm(len(target_text), time_elapsed)
    accuracy = calculate_accuracy(correct_chars, wrong_chars)
    date = datetime.datetime.now()

    stdscr.clear()
    stdscr.addstr(1, 5, f'WPM: {wpm}', curses.color_pair(5))
    stdscr.addstr(1, 15, f'Accuracy Percentage: {accuracy}', curses.color_pair(5))
    stdscr.addstr(2, 5, f'Duration: {time_elapsed:.2f} seconds', curses.color_pair(5))
    stdscr.refresh()
    stdscr.getch()

    record_manager.insert_record(wpm, accuracy, correct_chars, wrong_chars, date.strftime('%Y-%m-%d %H:%M'))


def calculate_wpm(letters_count, time_elapsed):
    return round((letters_count / 5) / (time_elapsed / 60))


def calculate_accuracy(correct_chars, wrong_chars):
    return round(correct_chars * 100 / (correct_chars + wrong_chars))
