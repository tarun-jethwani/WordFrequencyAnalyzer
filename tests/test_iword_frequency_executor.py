""" This module contains test cases for IWordFrequencyExecutor Class """
import unittest
# to mock builtins input() method
from unittest.mock import patch

from tests.test_data.inputs import INVALID_NUM_STRING, NUM_STRING, PARAMS

from ..src.constants import OPTIONS_MAP
from ..src.iword_frequency_executor import IWordFrequencyExecutor


class MyTestCase(unittest.TestCase):
    """
    this test class test methods of IWordFrequencyExecutor
    class, tests valid user inputs and reset of options map
    """
    @classmethod
    def setUpClass(cls) -> None:
        """
        creates instance of IWordFrequencyExecutor class, providing
        OPTIONS_MAP as argument
        """
        cls.executor = IWordFrequencyExecutor(OPTIONS_MAP)

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.executor

    @patch('builtins.input', return_value=NUM_STRING)
    def test_get_user_option(self, _):
        self.executor.get_option_from_user()
        self.assertEqual(self.executor.user_option, 3)

    @patch('builtins.input', return_value=INVALID_NUM_STRING)
    def test_value_error_in_user_option(self, _):
        """
        if the option entered by user is invalid, it raises
        ValueError, assert for ValueError where user enters
        invalid option
        """
        self.assertRaises(ValueError, self.executor.get_option_from_user)

    @patch('builtins.input', side_effect=PARAMS)
    def test_reset(self, _):
        """
        test whether the parameter or arguments of the options map
        at given option key by user, is none ( indicating the
        options map has been reset)
        """
        self.executor.get_function_arguments()
        self.executor.execute_function()
        value = self.executor.options_map[self.executor.user_option][
                                          'params']['text']
        self.assertEqual(value, None)
