#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
        el Test class
    """

    def test_standard(self):
        """ norm test
        """
        self.assertEqual(max_integer([1,6, 100, 4, 0, -1, 10]), 100)

    def test_none(self):
        """ None test
        """
        self.assertEqual(max_integer([]), None)

    def test_typdef(self):
        """ sending in string
        """
        self.assertEqual(max_integer("wasabi and chips"), 'w')

    def test_typedefArr(self):
        """ sending in arr with diff types
        """
        with self.assertRaises(TypeError):
            max_integer([1, "GILLET", 33, "THE BEST A MAN CAN GET", 7])

    def test_negativeArr(self):
        """ sending only negative nums
        """
        self.assertEqual(max_integer([-1, -33, -7]), -1)

if __name__ == '__main__':
    unittest.main()
