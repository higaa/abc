import unittest

import calclib

class TestCalc(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_mult(self):
        self.assertEqual(calclib.mult(7, 8), 56)