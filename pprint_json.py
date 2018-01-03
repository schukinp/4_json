import json
import argparse


def get_file():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file')
    return parser.parse_args().file


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def pretty_print_json(loaded_data):
    return json.dumps(
        loaded_data,
        indent=4,
        sort_keys=True,
        ensure_ascii=False
                      )


if __name__ == '__main__':
    filepath = get_file()
    loaded_data = load_data(filepath)
    print(pretty_print_json(loaded_data))