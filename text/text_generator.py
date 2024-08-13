import random


def read_text_file(filename: str) -> list:
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


def generate_random_text() -> str:
    text_lines = read_text_file('text/typing_texts.txt')
    return random.choice(text_lines)
