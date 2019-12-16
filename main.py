import unittest
from fibseqfinder import FibValue
from NumberToString import NumToStringConverter

class getFibNumandConvertToString(unittest.TestCase):

    def setUp(self):
        self.fibNumber = FibValue().getFibNumValue(3)

    def test_convertNumber(self):
        self.NumConverter = NumToStringConverter(self.fibNumber)
        self.NumConverter.convert_number_to_string()


if __name__ == '__main__':
    unittest.main()