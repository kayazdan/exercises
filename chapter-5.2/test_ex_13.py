from ex_5_13 import calc_falling_distance

import unittest


class TestFallingDistance(unittest.TestCase):
    
    def test_one_second(self):
        expected = 4.905
        actual = calc_falling_distance(1)
        self.assertEqual(expected, actual)
        
    def test_zero_seconds(self):
        expected = 0
        actual = calc_falling_distance(0)
        self.assertEqual(expected, actual)
        
    
print(calc_falling_distance(1))


unittest.main()