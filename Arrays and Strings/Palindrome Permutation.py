test_cases = [
    {
        'input': 'tact coa',
        'output': True
    },
    {
        'input': 'tact coab',
        'output': False
    },
    {
        'input': 'tact coabb',
        'output': True
    },
    {
        'input': 'abcc',
        'output': False
    }
]
test_cases2 = [
    ("aba", True),
    ("aab", True),
    ("abba", True),
    ("aabb", True),
    ("a-bba", True),
    ("a-bba!", True),
    ("Tact Coa", True),
    ("jhsabckuj ahjsbckj", True),
    ("Able was I ere I saw Elba", True),
    ("So patient a nurse to nurse a patient so", False),
    ("Random Words", False),
    ("Not a Palindrome", False),
    ("no x in nixon", True),
    ("azAZ", True),
]

def palindrome_permutation(s):
    '''
    ? to lower case

    naive solution:
        no more than 2 chr can appear in odd times

    **remove all non-letter charators**
    '''
    s = ''.join([chr_.lower() for chr_ in s])
    s = ''.join([chr_ for chr_ in s if ord(chr_)<=122 and ord(chr_) >=97])
    odd_times_chr = dict()

    for chr_ in s:
        odd_times_chr[chr_] = 0
    for chr_ in s:
        odd_times_chr[chr_] += 1
    
    return len([k for (k,v) in odd_times_chr.items() if v%2!=0]) < 2

if __name__ == '__main__':
    for test in test_cases:
        assert palindrome_permutation(test['input']) == test['output'], f"{test[0]}, {test[1]}"
    for test in test_cases2:
        assert palindrome_permutation(test[0]) == test[1], f"{test[0]}, {test[1]}"
    
    print('test done!')
    
