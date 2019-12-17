import unittest
from fibseqfinder import FibValue
from NumberToString import NumToStringConverter

class getFibNumandConvertToString(unittest.TestCase):

    def setUp(self):
        self.fibNumber = FibValue()

    def test_convertNumber(self):
        for i in range(0, 40):
            self.NumConverter = NumToStringConverter(self.fibNumber.getFibNumValue(i))
            self.NumConverter.convert_number_to_string()


if __name__ == '__main__':
    unittest.main()