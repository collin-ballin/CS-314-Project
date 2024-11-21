###############################################################################
#
#   ********************************************************************
#   ****    "T_E_S_T_I_N_G"                 M O D U L E ...         ****
#   ****                                                            ****
#   ****     UNIT TESTS FOR:               "Cstring" class          ****
#   ****                                                            ****
#   ********************************************************************
#
#
###############################################################################
import unittest
from lib.utility.cstring import Cstring
from datetime import datetime


class TestCString(unittest.TestCase):
    def test_initialization_exact_size(self):
        """Test initialization with a string that exactly matches the size."""
        s = Cstring("Hello", 5)
        self.assertEqual(s.data, "Hello")
        self.assertEqual(s.size, 5)

    def test_initialization_long_string(self):
        """Test initialization with a string longer than the size (should truncate)."""
        s = Cstring("Hello, World!", 5)
        self.assertEqual(s.data, "Hello")
        self.assertEqual(s.size, 5)

    def test_initialization_short_string(self):
        """Test initialization with a string shorter than the size (should pad)."""
        s = Cstring("Hi", 5)
        self.assertEqual(s.data, "Hi   ")
        self.assertEqual(s.size, 5)

    def test_modify_value_valid_length(self):
        """Test modifying the value with a string of valid length."""
        s = Cstring("Hello", 5)
        s.data = "World"
        self.assertEqual(s.data, "World")
        self.assertEqual(s.size, 5)

    def test_modify_value_long_string(self):
        """Test modifying the value with a string longer than size (should truncate)."""
        s = Cstring("Hello", 5)
        s.data = "Python"
        self.assertEqual(s.data, "Pytho")
        self.assertEqual(s.size, 5)

    def test_modify_value_short_string(self):
        """Test modifying the value with a string shorter than size (should pad)."""
        s = Cstring("Hello", 5)
        s.data = "Hi"
        self.assertEqual(s.data, "Hi   ")
        self.assertEqual(s.size, 5)

    def test_immutable_size(self):
        """Test that the size attribute is immutable."""
        s = Cstring("Hello", 5)
        with self.assertRaises(AttributeError):
            s.size = 10

    def test_str_representation(self):
        """Test the string representation of the Cstring object."""
        s = Cstring("Hello", 5)
        self.assertEqual(str(s), "Hello")

    def test_repr_representation(self):
        """Test the repr representation of the Cstring object."""
        s = Cstring("Hello", 5)
        self.assertEqual(repr(s), "Cstring(value='Hello', size=5)")

    def test_invalid_initialization_type(self):
        """Test initialization with non-string input (should raise TypeError)."""
        with self.assertRaises(TypeError):
            Cstring(12345, 5)  # Non-string value

    def test_invalid_size_type(self):
        """Test initialization with non-integer size (should raise TypeError)."""
        with self.assertRaises(TypeError):
            Cstring("Hello", "5")  # Non-integer size
