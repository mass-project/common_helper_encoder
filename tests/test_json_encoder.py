import unittest
from common_helper_encoder.json_encoder import ReportEncoder


class Test_json_encoder(unittest.TestCase):

    def setUp(self):
        self.encoder = ReportEncoder()

    def test_byte_encoding(self):
        input_data = b'TEST'
        result = self.encoder.default(input_data)
        self.assertEqual(result, "VEVTVA==", "base64 encoding not correct")


if __name__ == "__main__":
    unittest.main()
