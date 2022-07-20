test_cases = [
    ('pale', 'ple', True),
    ('pales', 'pale', True),
    ('pale', 'bale', True),
    ('pale', 'bake', False),
    ('aaa', 'aab', True),
    ('aaa', 'aaaa', True),
    ('abcd', 'bcda', False)
]

def one_away(s1, s2):
    overlapped_len = len( set(s1) & set(s2) )

    if abs(len(s1) - len(s2)) > 1:
        return False

    # remove and insert
    elif abs(len(s1) - len(s2)) == 1:
        if abs( len(set(s1)) - overlapped_len ) <= 1:
            return True
    
    # replace
    elif abs(len(s1) - len(s2)) == 0:
        # same string and a classic one away string
        if abs( len(set(s1)) - overlapped_len ) <= 1:
            return True

if __name__ == '__main__':
    for test in test_cases:
        assert one_away(test[0], test[1]) == test[2], f'{test}'
    
    print('all done')