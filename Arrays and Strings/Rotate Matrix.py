test_cases = [
    ([[1,2,3]], [[1], [2], [3]]),
    ([[1], [2], [3]], [[3,2,1]]),
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
    )
]

def rotate_matrix(matrix):
    '''
    Assume no 0x0. The smallest is 1x1.
    '''
    width = len(matrix[0])
    height = len(matrix)

    new_matrix = [
        [] * width
    ]
    
    i = 0
    
    while i:
        j = height - 1
        while j >= 0:
            new_matrix[i].append(matrix[j][i])
            # append on same row
            j -= 1
        # change to next row
        i += 1
        
    