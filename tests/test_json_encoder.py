import unittest
from common_helper_encoder.json_encoder import ReportEncoder
import datetime


class Test_json_encoder(unittest.TestCase):

    def setUp(self):
        self.encoder = ReportEncoder()

    def test_byte_encoding(self):
        input_data = b'TEST'
        result = self.encoder.default(input_data)
        self.assertEqual(result, "VEVTVA==", "base64 encoding not correct")

    def test_datetime_encoding(self):
        input_data = datetime.datetime(1970, 4, 23, 19, 00, 24)
        result = self.encoder.default(input_data)
        self.assertEqual(result, "1970-04-23T19:00:24")


if __name__ == "__main__":
    unittest.main()
