# csv.py
# to allow user to import data with csv

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# function which will open the csv file and read in its values and return
def import_csv(file_path):

    df = pd.read_csv(file_path, header=None)    # call function to read csv file into dataframe and pass params as there are no headers

    x_values = np.array(df[0].tolist()) # to convert column into a list and store it in numpy array format
    y_values = np.array(df[1].tolist())

    return x_values, y_values	# return numpy arrays


def plot_graph(x_values, y_values, b_m, r_2):

    plt.scatter(x_values, y_values, label="Sample data")

    yhat = np.array(b_m[1] * x_values + b_m[0])
    plt.plot(x_values, yhat, 'r', label=f'y={b_m[1]:6.5e}x+{b_m[0]:6.5e}')

    # show graph and save figure
    plt.xlabel("X")   # set the graph attributes
    plt.ylabel("Y")
    plt.title(f"Linear Regression using Least Squares Method (R\u00b2 = {r_2:6.5e})")
    plt.tight_layout()
    # plt.savefig('data/linear_regression.png')
    plt.text(2, 6, "hello", fontsize=15)
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()
    plt.ion()

    input("\nEnter to return to menu...")   # pause the program to show graph
    plt.close('all')




# plot_graph(x_values, y_values, b_m, r_2)

