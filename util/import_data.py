# csv.py
# import data from csv file and convert it to numpy array
# plot scatter graph

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# function which will open the csv file and read its values and return numpy arrays
def import_csv(file_path):

    df = pd.read_csv(file_path, header=None)    # call function from pandas module to read csv file into dataframe and pass params as there are no headers

    x_values = np.array(df[0].tolist()) # to convert column into a list and store it in numpy array
    y_values = np.array(df[1].tolist())

    return x_values, y_values	# return numpy arrays

# function to plot scatter graph with data set and linear regression line
def plot_graph(x_values, y_values, b_m, r_2):

    plt.scatter(x_values, y_values, label="Sample data")    # plot points on graph

    y_line = np.array(b_m[1] * x_values + b_m[0]) # find the y values for the linear regression line
    plt.plot(x_values, y_line, 'r', label=f'y={b_m[1]:6.5e}x+{b_m[0]:6.5e}')    # plot the linear regression line on graph

    # set the graph attributes, show graph and save figure
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(f"Linear Regression using Least Squares Method (R\u00b2 = {r_2:6.5e})")
    plt.grid()
    plt.tight_layout()
    plt.legend(loc='upper left')
    plt.savefig('data/linear_regression.png')
    plt.show()
    plt.ion()

    input("\nEnter to return to menu...")   # pause the program to show graph
    plt.close('all')
