import numpy as np


def arrays():
    arr_1 = np.eye(3)
    arr_2 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=float)
    arr_3 = np.full((3, 3), 0)
    return


def matrix_multiplication(m1, m2):
    return np.matmul(m1, m2)


def multiplication_check(matrices):
    for m in range(len(matrices) - 1):
        if len(matrices[m][0]) != len(matrices[m + 1]):
            return False
    return True


def multiply_matrices(matrices):
    if multiplication_check(matrices) is False:
        return
    else:
        res = matrices[0]
        for m in matrices[1:]:
            res = np.matmul(res, m)
        return res


def compute_2d_distance(arr1, arr2):
    return np.sqrt(np.sum((arr1 - arr2) ** 2))


def compute_multidimensional_distance(arr1, arr2):
    return np.sqrt(np.sum((arr1 - arr2) ** 2))


def compute_pair_distances(matrix):
    x = np.sum(matrix ** 2, axis=1)
    y = np.sum(matrix ** 2, axis=1)
    xy = np.matmul(matrix, matrix.T)
    x = x.reshape(-1, 1)
    dist_matrix = np.sqrt(x - 2 * xy + y)
    return dist_matrix

