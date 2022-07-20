test_cases = [
    ('aabcccccaaa', 'a2b1c5a3'),
    ('abcd', 'abcd'),
    ('abb', 'abb')
]


def string_comporession(str_):
    '''
    brute force
    '''
    new_str = ''
    for i, chr_ in enumerate(str_):
        new_str += f'{chr_}1'
        
        if len(new_str) > 2:
            pre_chr = new_str[]


def string_comporession_wrong(str_):
    '''
    brutal for loop to replace duplicated char w/ number
    then check if the size is shrinken
    '''
    new_str_dict = dict()
    for chr_ in set(str_):
        new_str_dict[chr_] = 0
    for chr_ in str_:
        new_str_dict[chr_] += 1

    new_str = ''
    for (k, v) in new_str_dict.items():
        new_str += f'{k}{v}'

    
    return str_ if len(new_str) >= len(str_) else new_str


if __name__ == '__main__':
    for test in test_cases:
        assert string_comporession(test[0]) == test[1], f'{test}, {string_comporession(test[0])}'
    print('all done')
    
        