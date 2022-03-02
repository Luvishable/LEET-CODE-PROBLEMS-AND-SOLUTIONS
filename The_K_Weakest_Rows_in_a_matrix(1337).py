"""

EXPLANATION OF QUESTION

You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians).
The soldiers are positioned in front of the civilians.
That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.
"""

def kWeakestRows(matrix,k):

    m = len(matrix)
    n = len(matrix[0])

    strengths = []
    for i, row in enumerate(matrix):
        strength = 0
        for j in range(n):
            if row[j] == 0:
                break
            strength += 1
        strengths.append((strength,i))

    strengths.sort()

    indexes = []
    for i in range(k):
        indexes.append(strengths[i][1])
    return indexes


