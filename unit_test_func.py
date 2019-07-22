import unittest
from function import math_sum

class TestCase(unittest.TestCase):
    
    def test_math_sum(self):
        right_answer = math_sum(1, 2)
        self.assertEqual(right_answer, 3)


unittest.main()
        