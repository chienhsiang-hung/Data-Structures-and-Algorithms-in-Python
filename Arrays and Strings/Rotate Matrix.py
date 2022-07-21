import unittest

            # [
            #     [1,2,3],
            #     [4,5,6],
            #     [7,8,9]
            # ],
            # [
            #     [7,4,1],
            #     [8,5,2],
            #     [9,6,3]
            # ]

def rotate_matrix_InPlace(matrix):
    '''
    for NxN square matrix
    '''
    item = len(matrix) - 1
    layer = item - 2

    i = 0
    while i <= layer:
        j = i
        while j <= item:
            matrix[i][j] = matrix[j][item-i]
            matrix[j][item-i] = matrix[item-i][item-j]
            matrix[item-i][item-j] = matrix[item-j][i]
            matrix[item-j][i] = matrix[i][j]
            print(matrix)
            
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

    def test_rotate_matrix(self):
        for function in self.test_functions:
            for (_input, _output) in self.test_cases:
                assert function(_input) == _output, f'{_input}, {_output}, {function(_input)}'

if __name__ == '__main__':
    for (_input, _output) in Test.test_cases:
        assert rotate_matrix_InPlace(_input) == _output, f'{_input}, {_output}, {rotate_matrix_InPlace(_input)}'
    print('all done')

    test_list = [[]]*5
    print(id(test_list[0]) == id(test_list[1]))
    # unittest.main()