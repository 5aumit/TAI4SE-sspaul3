def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))

import unittest
class TestIsBalanced(unittest.TestCase):

    def test_is_balanced(self):
        self.assertEquals(descending_order(0), 0)
        self.assertEquals(descending_order(15), 51)
        self.assertEquals(descending_order(123456789), 987654321)
        self.assertEquals(descending_order(1201), 2110)

if __name__ == '__main__':
    unittest.main()
