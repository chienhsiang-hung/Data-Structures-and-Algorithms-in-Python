test_cases = [
    ('aabcccccaaa', 'a2b1c5a3'),
    ('abcd', 'abcd'),
    ('abb', 'abb'),

        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
]


def string_comporession(str_):
    '''
    brute force
    '''
    new_str = ''
    for i, chr_ in enumerate(str_):
        new_str += f'{chr_}1'
        
        if len(new_str) > 2:
            pre_chr = new_str[-4]
            pre_num = new_str[-3]
            pos_chr = new_str[-2]
            pos_num = new_str[-1]

            if pre_chr == pos_chr:
                new_str = new_str[:-3] + str( int(pre_num) + 1 )
    return str_ if len(new_str) >= len(str_) else new_str



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
    
        