#!/usr/bin/python3
"""
Contains the matrix_mul function
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices (lists of lists of integers/floats)"""
    if type(m_a) is not list or not all(isinstance(i, list) for i in m_a):
        raise TypeError("m_a must be a list of lists")
    if type(m_b) is not list or not all(isinstance(i, list) for i in m_b):
        raise TypeError("m_b must be a list of lists")
    
    if not m_a or not m_b:  # Checks if either m_a or m_b is empty
        raise ValueError("m_a can't be empty" if not m_a else "m_b can't be empty")
    
    l1 = len(m_a)
    l2 = len(m_a[0])
    for row in m_a:
        if len(row) != l2:
            raise TypeError("each row of m_a must be of the same size")
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("m_a should contain only integers or floats")
    
    l3 = len(m_b[0])
    for row in m_b:
        if len(row) != l3:
            raise TypeError("each row of m_b must be of the same size")
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("m_b should contain only integers or floats")
    
    if l2 != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    # Perform matrix multiplication
    result_matrix = []
    for i in range(l1):
        result_row = []
        for j in range(l3):
            sum = 0
            for k in range(l2):
                sum += m_a[i][k] * m_b[k][j]
            result_row.append(sum)
        result_matrix.append(result_row)
    
    return result_matrix
