test_cases = [
    ('pale', 'ple', True),
    ('pales', 'pale', True),
    ('pale', 'bale', True),
    ('pale', 'bake', False),
    ('aaa', 'aab', True),
    ('aaa', 'aaaa', True),
    ('abcd', 'bcda', False),

        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False),

        # no changes
        ("pale", "pale", True),
        ("", "", True),
        # one insert
        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pales", "pale", True),
        ("ples", "pales", True),
        ("pale", "pkle", True),
        ("paleabc", "pleabc", True),
        ("", "d", True),
        ("d", "de", True),
        # one replace
        ("pale", "bale", True),
        ("a", "b", True),
        ("pale", "ble", False),
        # multiple replace
        ("pale", "bake", False),
        # insert and replace
        ("pale", "pse", False),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
        # permutation with insert shouldn't match
        ("ale", "elas", False),        
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
    # 1. distinguish long s and short s
    (longS, shortS) = (s1, s2) if len(s1) > len(s2) else (s2, s1)
    
    # 2. kick out those len dif > 1
    if len(longS) - len(shortS) > 1:
        return False
    else:
        # 3. find the extra one
        for i in range( len(shortS) ):
            if longS[i] != shortS[i]:
                return longS[i+1:] == shortS[i:]
        return True
                
            
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