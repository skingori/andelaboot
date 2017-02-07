import unittest
from main import is_prime

class PrimesTestCase(unittest.TestCase):

    def test_one_prime(self):
        self.assertTrue(is_prime(7))

    def test_two_not_prime(self):
        self.assertFalse(is_prime(0))

    def test_three_four(self):
        self.assertFalse(is_prime(4))
        """"more""""




if __name__ == '__main__':
    unittest.main()
