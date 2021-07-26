def vector_size_check(*vector_variables):
    return len(set([len(vector) for vector in vector_variables])) == 1


def vector_addition(*vector_variables):
    if not vector_size_check(*vector_variables):
        return ArithmeticError

    return [sum(t) for t in zip(*vector_variables)]


def vector_subtraction(*vector_variables):
    if not vector_size_check(*vector_variables):
        raise ArithmeticError

    minus_sum = [-sum(t) for t in zip(*vector_variables)]
    first_vector = vector_variables[0]

    return [2 * first_vector[i] + minus_sum[i] for i in range(len(minus_sum))]


def scalar_vector_product(alpha, vector_variable):
    return [alpha * v for v in vector_variable]


def matrix_size_check(*matrix_variables):
    size_list = [[len(matrix[0]), len(matrix)] for matrix in matrix_variables]
    tf_vector = [len(set(each_size)) == 1 for each_size in zip(*size_list)]
    return tf_vector[0] * tf_vector[1] == 1


def is_matrix_equal(*matrix_variables):
    return None


def matrix_addition(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    return [[sum(row) for row in zip(*t)] for t in zip(*matrix_variables)]


def matrix_subtraction(*matrix_variables):
    if not matrix_size_check(*matrix_variables):
        raise ArithmeticError
    minus_sum = [-sum(t) for t in zip(*matrix_variables)]
    first_vector = matrix_variables[0]

    return [2 * first_vector[i] + minus_sum[i] for i in range(len(minus_sum))]


def matrix_transpose(matrix_variable):
    return [[e for e in t] for t in zip(*matrix_variable)]


def scalar_matrix_product(alpha, matrix_variable):
    return [[alpha * e for e in row] for row in matrix_variable]


def is_product_availability_matrix(matrix_a, matrix_b):
    return matrix_size_check(matrix_a, matrix_transpose(matrix_b))


def matrix_product(matrix_a, matrix_b):
    if not is_product_availability_matrix(matrix_a, matrix_b):
        raise ArithmeticError
    return [[sum(a * b for a, b in zip(row_a, column_b)) for column_b in zip(*matrix_b)] for row_a in matrix_a]


if __name__ == '__main__':
    print(matrix_product([[1, 2], [3, 4, 5]], [[3, 2, 1], [3, 4]]))
