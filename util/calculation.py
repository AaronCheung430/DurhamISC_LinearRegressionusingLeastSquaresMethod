# calcuation.py
# calculate linear regession line and correlation coefficient

import numpy as np
import copy

# funtion to inverse the 2x2 matrix
def inverse_matrix(normal_matrix):

    scalar = 1 / ((normal_matrix[0][0] * normal_matrix[1][1]) - (normal_matrix[0][1] * normal_matrix[1][0]))
    # scalar = np.linalg.det(normal_matrix))    # the code above could be replace by this line, and this is also applicable for different size of matrix

    inversed_matrix = copy.deepcopy(normal_matrix)  # deepcopy the normal_matrixto inversed_matrix to store in another memory

    # inverse the matrix manually
    inversed_matrix[0][0] = normal_matrix[1][1]
    inversed_matrix[0][1] = -normal_matrix[1][0]
    inversed_matrix[1][0] = -normal_matrix[0][1]
    inversed_matrix[1][1] = normal_matrix[0][0]

    # iterate through rows and columns of the matrix
    for row in range(len(inversed_matrix)):
        for column in range(len(inversed_matrix[row])):
            # replace the value in the inversed_matrix after scalar multplication
            inversed_matrix[row][column] = inversed_matrix[row][column] * scalar

    return inversed_matrix  # return inversed matrix (a nested list)

# function to find the linear regression line
def find_linear_regress(x_values, y_values):

    # create nested array with ones and insert x_values as colomn and update x_values
    x_values = np.insert(np.ones((x_values.size, 1)), 1, x_values, axis=1)
    x_T_x = x_values.transpose().dot(x_values)
    x_T_y = np.dot(x_values.transpose(), y_values)

    x_T_x_inv = np.array(inverse_matrix(x_T_x.tolist()))    # convert x_T_x to list, and call function to find inversed matrix, then convert the return value to numpy array

    b_m = x_T_x_inv.dot(x_T_y)  # multiply both matrix to find A, the values for b and m

    verify_b_m = np.linalg.inv(x_values.transpose().dot(x_values)).dot(x_values.T).dot(y_values)  # the code above could be replace by this one line by using the function from numpy

    return b_m, verify_b_m  # return both variables in numpy array form

# function to find the correlation coefficient
def find_corr_coeff(x_values, y_values, b_m):

    e_values = np.array([y_values[i] - (b_m[1] * x_values[i] + b_m[0]) for i in range(len(x_values))])  # find matrix E
    sse = e_values.transpose().dot(e_values)    # find the sum of squares error

    sst = np.sum((y_values - np.mean(y_values)) ** 2)   # find the sum of squares total
    ssr = sst - sse # find the sum of squares regression
    r_2 = ssr / sst # find the r^2 value

    verify_r_2 = (np.corrcoef(x_values, y_values)[0,1])**2  # the code above could be replace by this one line by using the function from numpy

    return r_2, verify_r_2  # return both variables
