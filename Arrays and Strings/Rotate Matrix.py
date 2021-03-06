import unittest
from copy import deepcopy
from collections import defaultdict
import time

# [[21, 16, 11, 6, 1], 
# [22, 17, 8, 7, 2], 
# [23, 12, 13, 14, 3], 
# [24, 19, 18, 9, 4], 
# [25, 20, 15, 10, 5]]

# [[21, 16, 11, 6, 1], 
# [22, 17, 12, 7, 2], 
# [23, 18, 13, 8, 3], 
# [24, 19, 14, 9, 4], 
# [25, 20, 15, 10, 5]]

# [[21, 16, 11, 6, 1], 
# [22, 19, 12, 17, 2], 
# [23, 18, 13, 8, 3], 
# [24, 9, 14, 7, 4], 
# [25, 20, 15, 10, 5]]

def rotate_matrix_InPlace(matrix):
    '''
    for NxN square matrix
    '''
    item = len(matrix) - 1
    layer = item - 2

    i = 0
    while i <= layer:
        j = i
        while j <= item -1 -i:
            # (0,0) -> (0,2), (0,2) -> (2,2),    (2,2) -> (2,0),       (2,0) -> (0,0)
            matrix[i][j], matrix[j][item-i], matrix[item-i][item-j], matrix[item-j][i] = matrix[item-j][i], matrix[i][j], matrix[j][item-i], matrix[item-i][item-j]
            # i = 1, j = 3, item = 4
            # (1, 3), (3, 3), (3, 1), (1, 1)
            
            j += 1
        i += 1
    return matrix

def rotate_matrix(matrix):
    '''
    Assume no 0x0. The smallest is 1x1.
    '''
    width = len(matrix[0])
    height = len(matrix)

    new_matrix = []
    i = 0
    while i < width:
        new_matrix.append([]) # add a row
        j = height - 1
        while j >= 0:
            new_matrix[i].append(matrix[j][i])
            # append on same row
            j -= 1
        # change to next row
        i += 1
    
    return new_matrix


# this way, all the inner list will be pointed to the same address
# i.e.
# test_list = [[]]*5
# id(test_list[0]) == id(test_list[1])
def rotate_matrix_wrong(matrix):
    '''
    Assume no 0x0. The smallest is 1x1.
    '''
    width = len(matrix[0])
    height = len(matrix)

    new_matrix = [ [None]*height ] * width

    i = 0
    while i < width:
        j = height - 1
        while j >= 0:
            print(j, i, matrix[j][i], new_matrix[i])
            new_matrix[i][j] = matrix[j][i]
            print(new_matrix[i], new_matrix)
            # append on same row
            j -= 1
        # change to next row
        i += 1
    
    return new_matrix


class Test(unittest.TestCase):
    test_cases = [
        # (
        #     [
        #         [1, 2, 3]
        #     ],
        #     [
        #         [1],
        #         [2],
        #         [3]
        #     ]
        # ),
        # ([[1], [2], [3]], [[3,2,1]]),
        ### it's an NxN matrix ###
        (
            [
                [1,2,3],
                [4,5,6],
                [7,8,9]
            ],
            [
                [7,4,1],
                [8,5,2],
                [9,6,3]
            ]
        ),

            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
            (
                [
                    [1, 2, 3, 4, 5],
                    [6, 7, 8, 9, 10],
                    [11, 12, 13, 14, 15],
                    [16, 17, 18, 19, 20],
                    [21, 22, 23, 24, 25],
                ],
                [
                    [21, 16, 11, 6, 1],
                    [22, 17, 12, 7, 2],
                    [23, 18, 13, 8, 3],
                    [24, 19, 14, 9, 4],
                    [25, 20, 15, 10, 5],
                ],
            ),
    ]
    testable_functions = [
        rotate_matrix_InPlace,
        rotate_matrix
    ]

    # def test_rotate_matrix(self):
    #     for function in self.testable_functions:
    #         print(function)
    #         for (_input, _output) in self.test_cases:
    #             _input = deepcopy(_input) # don't forget this line, because it changes original input that make your right answer to be wrong
    #             assert function(_input) == _output, f'{_input}, {_output}, {function(_input)}'

    def test_rotate_matrix(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)
        for _ in range(num_runs):
            for text, expected in self.test_cases:
                _input = deepcopy(text) # don't forget this line, because it changes original input that make your right answer to be wrong
                for func in self.testable_functions:
                    start = time.perf_counter()
                    func(_input)
                    assert(
                        _input == expected
                    ), f'{func.__name__} failed for value: {text}, output={_input}, expected={expected}'

                    function_runtimes[func.__name__] += (time.perf_counter() - start) * 1000
        print(f'\n{num_runs} runs')
        for function_name, runtime in function_runtimes.items():
            print(f'{function_name}: {runtime:.1f}ms')

if __name__ == '__main__':
    # for (_input, _output) in Test.test_cases:
    #     print(id(_input), id(_output))
    #     print(_input, _output)
    #     assert rotate_matrix_InPlace(_input) == _output, f'{_input}, {_output}, {rotate_matrix_InPlace(_input)}'
    #     print(f'{_input}, {_output}, {rotate_matrix_InPlace(_input)}')
    # print('all done')

    # test_list = [[]]*5
    # print(id(test_list[0]) == id(test_list[1]))
    unittest.main()