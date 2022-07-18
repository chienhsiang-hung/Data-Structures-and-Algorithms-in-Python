import time
import unittest
from collections import defaultdict

def is_unique_set(s):
    return len(set(s)) == len(s)

class Test(unittest.TestCase):
    test_cases = [
        ('abcd', True),
        ('1234', True),
        ('a3g4ss', False),
        ('', True),
        ('<<', False),
        ('<5*8o jc', True),
        ('  ', False),
        (''.join([chr(i) for i in range(100)]), True), # unique 128 chars
        (''.join([chr(i) for i in range(1000)]+['A']), False) # non-unique 1001 chars
    ]
    test_functions = [
        is_unique_set
    ]

    def test_is_unique_chars(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)
        for _ in range(num_runs):
            for text, expected in self.test_cases:
                for is_unique_chars in self.test_functions:
                    start = time.perf_counter()
                    assert(
                        is_unique_chars(text) == expected
                    ), f'{is_unique_chars.__name__} failed for value: {text}'

                    function_runtimes[is_unique_chars.__name__] += (time.perf_counter() - start) * 1000
        print(f'\n{num_runs} runs')
        for function_name, runtime in function_runtimes.items():
            print(f'{function_name}: {runtime:.1f}ms')

if __name__ == "__main__":
    unittest.main()