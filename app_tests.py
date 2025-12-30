import unittest
from app import calculate_sum

class TestProgressionSum(unittest.TestCase):
    
    def test_standard_cases(self):
        self.assertEqual(calculate_sum(1), 1)
        self.assertEqual(calculate_sum(2), 5)
        self.assertEqual(calculate_sum(3), 12)

    def test_zero(self):
        self.assertEqual(calculate_sum(0), 0)

    def test_negative_input(self):
        with self.assertRaises(TypeError):
            calculate_sum(-1)

if __name__ == '__main__':
    unittest.main()