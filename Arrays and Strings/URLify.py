test_cases = [
    {'input': {
        's': 'abc aa ',
        'l': 6
        },
    'output': 'abc%20aa'},
    {'input': {
        's': 'abc aa 57%20 ',
        'l': 13
        },
    'output': 'abc%20aa%2057%20%20'},
    {'input': {
        's': ' abc aa 57%20 ',
        'l': 14
        },
    'output': '%20abc%20aa%2057%20%20'},
    {'input': {
        's': 'much ado about nothing      ',
        'l': 22
        },
    'output': 'much%20ado%20about%20nothing'},
    {'input': {
        's': 'Mr John Smith       ',
        'l': 13
        },
    'output': 'Mr%20John%20Smith'},
    {'input': {
        's': ' a b    ',
        'l': 4
        },
    'output': '%20a%20b'},
    {'input': {
        's': ' a b       ',
        'l': 5
        },
    'output': '%20a%20b%20'}
]

def URLify(s, l):
    # eliminate the (extra) ending space
    return s[:l].replace(' ', '%20')

if __name__ == '__main__':
    for test in test_cases:
        assert (
            URLify(**test['input']) == test['output']
        ), f"{test['input']}, {test['output']}"
    print('done test!')