import binascii
import hashlib
import unittest

# from gcode_parser import GcodeParser

class TestParseGcode(unittest.TestCase):
    # def test_parse_gcode(self):
    #     """
    #     Test that it can sum a list of integers
    #     """
    #     with open('star.gcode', 'r') as f:
    #       gcode = f.read()
    #     parser = GcodeParser(gcode)
    #     for l in parser.lines:
    #       print(l)
        # self.assertEqual(result, 6)
    
    def test_other_thing(self):
        wskey = "dGhlIHNhbXBsZSBub25jZQ=="
        magicString = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
        # acceptkey = decoded + magicString.encode()
        c = wskey + magicString
        acceptkey = c.encode()
        h = hashlib.sha1(acceptkey)
        result = binascii.b2a_base64(h.digest()).decode().replace("\n", "")
        print(result)

        self.assertEqual(result, "s3pPLMBiTxaQ9kYGzzhZRbK+xOo=")


if __name__ == '__main__':
    unittest.main()
