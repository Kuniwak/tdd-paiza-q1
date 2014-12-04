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

    def test_get_product_count_2(self):
        raw_input = create_raw_input([10, 20])
        input_lines = raw_input

        actual_product_count = mission1.get_product_count(input_lines)

        expected_product_count = 2
        self.assertEqual(actual_product_count, expected_product_count)


if __name__ == '__main__':
    unittest.main()
