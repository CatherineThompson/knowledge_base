import unittest

from gcode_parser import GcodeParser

class TestParseGcode(unittest.TestCase):
    def test_parse_gcode(self):
        """
        Test that it can sum a list of integers
        """
        with open('star.gcode', 'r') as f:
          gcode = f.read()
        parser = GcodeParser(gcode)
        for l in parser.lines:
          print(l)
        # self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
