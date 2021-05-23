# calcuation.py
# calculate linear regession line and correlation coefficient

import numpy as np
import copy


x_values = np.array([0.85, 0.8, 0.75, 0.7, 0.65, 0.6, 0.55, 0.5, 0.45, 0.4,  0.35, 0.3])
y_values = np.array([37.16, 36.2, 34.96, 33.93, 32.82, 31.38, 30., 28.76, 27.32, 25.66, 24.09, 22.24])
b_m = np.array([14.9031352, 26.91048951])


def find_linear_regress(x_values, y_values):

    # create nested array with ones and insert x_values as colomn and update x_values
    x_values = np.insert(np.ones((x_values.size, 1)), 1, x_values, axis=1)
    x_T_x = x_values.transpose().dot(x_values)
    x_T_y = np.dot(x_values.transpose(), y_values)

    x_T_x_inv = np.array(inverse_matrix(x_T_x.tolist()))

    b_m = x_T_x_inv.dot(x_T_y)

    # print("hiii")
    # print(b_m)
    # print("The y-intercept is", b_m[0])
    # print("The gradient ", b_m[1])
    # print(f"The least squares regression line of this set of data is Y = {b_m[1]:.2f}x + {b_m[0]:.2f}")

    return b_m


def inverse_matrix(normal_matrix):

    scalar = 1 / ((normal_matrix[0][0] * normal_matrix[1][1]) - (normal_matrix[0][1] * normal_matrix[1][0]))
    # print(np.linalg.det(normal_matrix))

    inversed_matrix = copy.deepcopy(normal_matrix)  # deepcopy the normal_matrixto inversed_matrix to store in another memory

    inversed_matrix[0][0] = normal_matrix[1][1]
    inversed_matrix[0][1] = -normal_matrix[1][0]
    inversed_matrix[1][0] = -normal_matrix[0][1]
    inversed_matrix[1][1] = normal_matrix[0][0]

    # iterate through rows and columns of the matrix
    for row in range(len(inversed_matrix)):
        for column in range(len(inversed_matrix[row])):
            # replace the value in the inversed_matrix after scalar multplication
            inversed_matrix[row][column] = inversed_matrix[row][column] * scalar

    return inversed_matrix


# find_linear_regress(x_values, y_values)


def find_corr_coeff(x_values, y_values, b_m):

    e_values = np.array([y_values[i] - (b_m[1] * x_values[i] + b_m[0]) for i in range(len(x_values))])

    sse = e_values.transpose().dot(e_values)

    print(e_values)
    print(sse)






find_corr_coeff(x_values, y_values, b_m)

