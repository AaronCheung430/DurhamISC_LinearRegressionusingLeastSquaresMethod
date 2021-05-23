# csv.py
# to allow user to import data with csv

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x_values = np.array([0.85, 0.8, 0.75, 0.7, 0.65, 0.6, 0.55, 0.5, 0.45, 0.4,  0.35, 0.3])
y_values = np.array([37.16, 36.2, 34.96, 33.93, 32.82, 31.38, 30., 28.76, 27.32, 25.66, 24.09, 22.24])

# function which will open the csv file and read in its values and return
def import_csv(file_path):

    df = pd.read_csv(file_path, header=None)    # call function to read csv file into dataframe and pass params as there are no headers

    x_values = np.array(df[0].tolist()) # to convert column into a list and store it in numpy array format
    y_values = np.array(df[1].tolist())

    return x_values, y_values	# return numpy arrays


def plot_graph(x_values, y_values):

    plt.scatter(x_values, y_values)
    plt.title("Linear Regression Line")

    # show graph and save figure
    # plt.tight_layout()
    # plt.savefig('data/comparison_algorithms.png')
    plt.show()
    plt.ion()

    input("\nEnter to return to menu...")   # pause the program to show graph
    plt.close('all')

    pass


plot_graph(x_values, y_values)