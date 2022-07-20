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
    # replace
    if len(s1) == len(s2):
        replace_chr = 0
        for chr1, chr2 in zip(s1, s2):
            if chr1 != chr2:
                replace_chr += 1
            if replace_chr > 1:
                return False
        return True
    # insert, remove
    
            
def one_away_Wrong(s1, s2):
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

def one_away_Wrong1(s1, s2):
    '''
    Assume two strings are different in default
    '''
    if len( len(s1) - len(s2) ) > 1 or s1==s2:
        return False
    
    else:
        check_start = False
        for i in range( min(len(s1), len(s2)) ):
            
            if check_start:
                # remove
                pass

            if s1[i] != s2[i]:
                check_start = True

if __name__ == '__main__':
    for test in test_cases:
        assert one_away(test[0], test[1]) == test[2], f'{test}'
    
    print('all done')