import unittest
import mission1


def create_raw_input(stock_counts, has_last_line_break=True):
    lines = [str(line) for line in [len(stock_counts)] + stock_counts]
    if has_last_line_break:
        return '\n'.join(lines) + '\n'
    else:
        return '\n'.join(lines)



class TestMission1(unittest.TestCase):
    def test_get_product_count_1(self):
        raw_input = create_raw_input([10])
        input_lines = raw_input

        actual_product_count = mission1.get_product_count(input_lines)

        expected_product_count = 1
        self.assertEqual(actual_product_count, expected_product_count)

    def test_get_product_count_example_1(self):
        raw_input = create_raw_input([5, 10, 2, 3])
        input_lines = raw_input

        actual_product_count = mission1.get_product_count(input_lines)

        expected_product_count = 4
        self.assertEqual(actual_product_count, expected_product_count)

    def test_get_product_count_example_2(self):
        raw_input = create_raw_input([100, 23, 12])
        input_lines = raw_input

        actual_product_count = mission1.get_product_count(input_lines)

        expected_product_count = 3
        self.assertEqual(actual_product_count, expected_product_count)

    def test_get_stocks_example1(self):
        stocks = [5, 10, 2, 3]
        raw_input = create_raw_input(stocks)
        input_lines = raw_input

        actual_stocks = mission1.get_stocks(input_lines)

        expected_stocks = stocks
        self.assertEqual(actual_stocks, expected_stocks)

    def test_get_stocks_example2(self):
        stocks = [100, 23, 12]
        raw_input = create_raw_input(stocks)
        input_lines = raw_input

        actual_stocks = mission1.get_stocks(input_lines)

        expected_stocks = stocks
        self.assertEqual(actual_stocks, expected_stocks)

    def test_get_stocks_example2_with_no_last_line_break(self):
        stocks = [100, 23, 12]
        raw_input = create_raw_input(stocks, has_last_line_break=False)
        input_lines = raw_input

        actual_stocks = mission1.get_stocks(input_lines)

        expected_stocks = stocks
        self.assertEqual(actual_stocks, expected_stocks)

    def test_sum_stocks(self):
        stocks = [2]

        actual_sum_stocks = mission1.sum_stocks(stocks)

        expected_sum_stocks = 2
        self.assertEqual(actual_sum_stocks, expected_sum_stocks)

    def test_sum_stocks_example1(self):
        stocks = [5, 10, 2, 3]

        actual_sum_stocks = mission1.sum_stocks(stocks)

        expected_sum_stocks = 20
        self.assertEqual(actual_sum_stocks, expected_sum_stocks)

    def test_sum_stocks_example2(self):
        stocks = [100, 23, 12]

        actual_sum_stocks = mission1.sum_stocks(stocks)

        expected_sum_stocks = 135
        self.assertEqual(actual_sum_stocks, expected_sum_stocks)



if __name__ == '__main__':
    unittest.main()
