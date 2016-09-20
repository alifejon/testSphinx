import unittest


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, False)
    def test_something1(self):
        self.assertEqual(True, False)
    def test_something2(self):
        self.assertEqual(True, True)
    def test_something3(self):
        self.assertEqual(True, True)
    def test_something4(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
