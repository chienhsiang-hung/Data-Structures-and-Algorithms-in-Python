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
        'output': True
    }
]

def palindrome_permutation(s):
    '''
    ? to lower case

    naive solution:
        no more than 2 chr can appear in odd times
    '''
    odd_times_chr = dict()

    for chr_ in s:
        odd_times_chr[chr_] = 0
    for chr_ in s:
        odd_times_chr[chr_] += 1
    
    return len([k for (k,v) in odd_times_chr.items() if v%2!=0]) <= 2

if __name__ == '__main__':
    for test in test_cases:
        assert palindrome_permutation(test['input']) == test['output']
    
    print('test done!')
    
