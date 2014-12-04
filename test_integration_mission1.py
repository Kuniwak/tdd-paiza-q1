import unittest
import mission1


def create_input_lines(stocks):
    return stocks.split()


class TestIntegrationMission1(unittest.TestCase):
    def test_sum_stocks_by_example1(self):
        input_lines = create_input_lines('4\n5\n10\n2\n3\n')

        actual_sum_stocks = mission1.sum_stocks(input_lines)

        expected_sum_stocks = 20
        self.assertEqual(actual_sum_stocks, expected_sum_stocks)


    def test_sum_stocks_by_example2(self):
        input_lines = create_input_lines('3\n100\n23\n12\n')

        actual_sum_stocks = mission1.sum_stocks(input_lines)

        expected_sum_stocks = 135
        self.assertEqual(actual_sum_stocks, expected_sum_stocks)


if __name__ == '__main__':
    unittest.main()
