test_cases = [
    ([[1, 0, 3]], [[0, 0, 0]]),
    ([[1], [0], [3]], [[0], [0], [0]]),
    (
        [
            [1, 2, 3, 0],
            [3, 0, 4, 4],
            [1, 3, 4, 5],
            [5, 5, 5, 5],
            [8, 9, 1, 1]
        ],
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 0, 4, 0],
            [5, 0, 5, 0],
            [8, 0, 1, 0]
        ]
    )
]

def zero_matrix(matrix):
    zero_locs = []
    for r, _ in enumerate(matrix):
        for c, item in enumerate(matrix[r]):
            if item == 0:
                zero_locs.append((r, c))
    
    for zero_loc in zero_locs:
        for r, _ in enumerate(matrix):
            for c, item in enumerate(matrix[r]):
                if r==zero_loc[0] or c==zero_loc[1]:
                    matrix[r][c] = 0
    
    return matrix

if __name__ == '__main__':
    for (_input, _output) in test_cases:
        _input_copy = _input.copy()
        assert zero_matrix(_input_copy) == _output 
    print('all done')

        # in-place function should avoid to be execute multiple times on same test set
        # if zero_matrix(_input) != _output:
        #     print(_input, _output, zero_matrix(_input))
            