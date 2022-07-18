import time
import unittest
from collections import defaultdict

def permutation(s1, s2):
    '''
    Assume the same size
    '''
    if len(s1) != len(s2) or len(s1) == 0 or len(s2) == 0:
        return False
    return sorted(s1) == sorted(s2)

class Test(unittest.TestCase):
    test_cases = [
        ('abc', 'bca', True),
        ('', '123', False),
        ('1', '123', False),
        ('13=k', 'k3=1', True),
        ('  3', ' 3', False),
        ('ccc', 'ccc', True),
        ('cc', 'ccc', False)
    ]
    test_functions = [
        permutation
    ]

    def test_permutation(self):
        for check_permutation in self.test_functions:
            for str1, str2, expected in self.test_cases:
                assert check_permutation(str1, str2) == expected

if __name__ == '__main__':
    unittest.main()