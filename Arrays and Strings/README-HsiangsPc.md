## Creating a Matrix in Python without numpy
```python
new_matrix  = [ [None]*height ] *  width
```
This way, all the inner list will be pointed to the same address, i.e.
```python
test_list = [[]]*5
id(test_list[0]) == id(test_list[1])
```
Do something like this instead.
```python
new_matrix = []
i = 0
while i < width:
    new_matrix.append([]) # add a row
    j = height - 1
    while j >= 0:
        new_matrix[i].append(matrix[j][i])
```
See example [Data-Structures-and-Algorithms-in-Python/Rotate Matrix.py at main · chienhsiang-hung/Data-Structures-and-Algorithms-in-Python (github.com)](https://github.com/chienhsiang-hung/Data-Structures-and-Algorithms-in-Python/blob/main/Arrays%20and%20Strings/Rotate%20Matrix.py)
