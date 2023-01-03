import unittest
max_integer = __import__('6-max_integer').max_integer
class TestMaxInteger(unittest.TestCase):
    def test_max_integeri(self):
        numbers = [5, 2, 4, 8]
        self.assertTrue(numbers[3] == max_integer(numbers))
    def test_empty_list(self):
        numbers = []
        self.assertTrue(max_integer(numbers) is None)
if "__name__" == "__main__":
    unittest.main
