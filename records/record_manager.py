import csv


def read_csv(file_path: str) -> list:
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return [row for row in reader]


def insert_csv(file_path: str, data: list) -> None:
    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)


def read_records() -> list[list]:
    return read_csv('records/records.csv')


def insert_record(wpm: int, accuracy: int, correct_characters: int, wrong_characters: int, date: str) -> None:
    insert_csv('records/records.csv', [wpm, accuracy, correct_characters, wrong_characters, date])
