import unittest
from main.my_module import square


class TestMyModule(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(2), 4)
        self.assertEqual(square(3.0), 9.0)
        self.assertNotEqual(square(-3), -9)


if __name__ == '__main__':
    unittest.main()
