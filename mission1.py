import sys


def get_product_count(lines):
    first_line = lines[0]
    return int(first_line)


def get_stocks(lines):
    lines_without_first_line = lines[1:]
    return [int(line) for line in lines_without_first_line]


def sum_stocks(lines):
    return sum(get_stocks(lines))


if __name__ == '__main__':
    input_lines = sys.stdin.readlines()
    print(sum_stocks(input_lines))
