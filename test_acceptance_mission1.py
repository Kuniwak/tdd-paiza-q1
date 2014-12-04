import unittest
import subprocess


class TestAcceptanceMission1(unittest.TestCase):
    def test_exec_mission1(self):
        input_lines = '4\n5\n10\n2\n3\n'

        output = subprocess.check_output(['python3', 'mission1.py'],
                                         input=input_lines,
                                         universal_newlines=True)

        self.assertEqual(output, '20\n')

if __name__ == '__main__':
    unittest.main()
