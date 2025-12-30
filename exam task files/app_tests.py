import unittest
from app import calculate_sum

class TestProgressionSum(unittest.TestCase):
    
    def test_standard_cases(self):
        # n=1 -> Сума 1
        self.assertEqual(calculate_sum(1), 1)
        # n=2 -> 1, 4 -> Сума 5
        self.assertEqual(calculate_sum(2), 5)
        # n=3 -> 1, 4, 7 -> Сума 12
        self.assertEqual(calculate_sum(3), 12)

    def test_zero(self):
        # n=0 -> Сума 0
        self.assertEqual(calculate_sum(0), 0)

    def test_negative_input(self):
        # Перевіряємо, що n=-1 викликає помилку ValueError
        with self.assertRaises(ValueError):
            calculate_sum(-1)

if __name__ == '__main__':
    unittest.main()