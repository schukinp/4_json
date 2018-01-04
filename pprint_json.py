import json
import sys


def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception:
        print('File is empty')
    finally:
        exit()


def pretty_print_json(filepath):
    return json.dumps(filepath, indent=4,
                      sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    filepath = sys.argv[1]
    print(pretty_print_json(load_data(filepath)))