# DUISC IFY Programming Techniques
# Summative 2 - Linear Regression using Least Squares Method

# Student No: 2595161
# DUID: qwwk95
# CLASS CODE: SFSCS_PT

# ------------------------------- Imported Packages -------------------------------
# import os
# import time
# import csv
# from util import config as cfg
# from util import start as strt
# from util.adj_list import open_csv_file, output_adj_list_table
# import numpy
# import pandas
# import matplotlib.pyplot as plt


# ---------------------------------- Main Program ---------------------------------

def main():

    end_program = False # variable used to check if user wants to exit program

    # loop until end_program is True
    while not end_program:

        # call menu function and get user's choice
        option = strt.menu()

        if option == 1: # import a graph from csv
            # adjac_list = open_csv_file(cfg.read_file_path)
            # cfg.clear_screen()
            # cfg.time_animation(3, "CSV file imported successfully.")
            # cfg.countdown(4)
            print("option 1")

        elif option == 2: # output the adjacency list as a table
            print("option 2")
            # output_adj = output_adj_list_table(adjac_list)
            # print(output_adj)


        elif option == 3: # find MST using kruskal's algorithm
            print("option 3")

        elif option == 4: # find MST using prim's algorithm
            print("option 4")

        elif option == 5: # Create graph of monthly sales
            print("option 5")

        elif option == 6: # Create graph of monthly sales
            print("option 6")

        else: # option 7 - exit in controlled manner

            # set end_program Boolean to True
            end_program = True

            # output messages to user
            print("Thank you for using this program")
            print("Quitting Program...")

        #### END OF MAIN PROGRAM


if __name__ == "__main__":
    main()
