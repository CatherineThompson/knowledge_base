import unittest

from pygcode import Line



class TestParseGcode(unittest.TestCase):
    def test_upper(self):
      with open('../assets/star.gcode', 'r') as fh:
        for line_text in fh.readlines():
            line = Line(line_text)

            if line.block.words[0] == "G01":
              if len(line.block.words) > 2:
                x = line.block.words[2].value
                y = line.block.words[3].value
                print(line.block.words)
                print(x, y)
            # line.block.gcodes  # is your list of gcodes
            # line.block.modal_params  # are all parameters not assigned to a gcode, assumed to be motion modal parameters

if __name__ == '__main__':
    unittest.main()