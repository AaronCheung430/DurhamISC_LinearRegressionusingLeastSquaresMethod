# csv.py
# to allow user to import data with csv

import csv

# import pandas

read_path = "../data/test_data.csv"

# function which will open the csv file and read in its values and return
def import_csv(file_path):

    x_value, y_value = [], []

	# database = [] # create empty list

    with open(file_path, "r") as csv_file: # open file in read mode
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            x_value.append(float(row[0]))
            y_value.append(float(row[1]))

        print(x_value)
        print(y_value)


	# return database	# return a nested list



import_csv(read_path)