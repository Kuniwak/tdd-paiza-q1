def get_product_count(lines_str):
    first_line = lines_str.split()[0]
    return int(first_line)


def get_stocks(lines_str):
    lines_without_first_line = lines_str.split()[1:]
    return [int(line) for line in lines_without_first_line]


def sum_stocks(stocks):
    return sum(stocks)
