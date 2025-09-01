#Author: Galen Flanagan
#Fun Fact: A photo of mine is a famous internet meme template.

from typing import TypeVar
T = TypeVar('T', int, float, complex)


def kroneckerProduct(U: list[list[T]], V: list[list[T]]):
    """a method to generate the kronecker product of two matrices

    Args:
        U (list[list[T]]): the first matrix to be multiplied
        V (list[list[T]]): the second matrix to be multiplied

    Returns:
        list[list[T]]: a matrix that is the kronecker product of U and V
    """
    ans: list[list[T]] = [] #matrix will be nk rows and mp columns
    for u in U:
        for v in V:
            row: list[T] = []
            for u2 in u:
                for v2 in v:
                    row.append(u2*v2)
            ans.append(row)
    print(ans)
    return ans
