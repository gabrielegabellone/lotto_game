import unittest
from unittest.mock import patch

from lotto.input_bill_number import InputBillNumber


class TestInputBillNumber(unittest.TestCase):
    @patch("builtins.input")
    def test_enter_bill_number(self, mock_inputs):
        mock_inputs.side_effect = ["one", "6", "4.5", "5"]
        actual = InputBillNumber.enter_bill_number()
        expected = 5
        self.assertEqual(actual, expected, "Expected the method to return 5.")
    
    def test_is_valid_input_return_true(self):
        valid_input = [0, 1, 2, 3, 4, 5]
        for value in valid_input:
            test_value = InputBillNumber.is_valid_input(value)
            self.assertTrue(test_value, "Expected the method to return True.")
    
    def test_is_valid_input_return_false(self):
        not_valid_input = [6, 4.5, "4", None]
        for value in not_valid_input:
            test_value = InputBillNumber.is_valid_input(value)
            self.assertFalse(test_value, "Expected the method to return False.")
