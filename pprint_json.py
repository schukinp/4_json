import json
import sys


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def pretty_print_json(filepath):
    return json.dumps(filepath, indent=4, sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    try:
        filepath = sys.argv[1]
        print(pretty_print_json(load_data(filepath)))
    except (FileNotFoundError, ValueError, IndexError):
        print('Cannot read file')
