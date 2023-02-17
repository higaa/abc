import unittest

import strlib

class TestStr(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_makestr(self):
        self.assertEqual(strlib.makestr('hoge', 3, 4), 'hoge12')