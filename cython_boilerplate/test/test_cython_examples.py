import logging
import unittest

from cython_boilerplate import factorial

logging.basicConfig(level=logging.DEBUG)


class TestSTL(unittest.TestCase):

    def test_factorial(self):
        assert factorial(10) == 3628800

if __name__ == '__main__':
    unittest.main()
