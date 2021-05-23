# DUISC IFY Programming Techniques
# Summative 2 - Linear Regression using Least Squares Method

# Student No: 2595161
# DUID: qwwk95
# CLASS CODE: SFSCS_PT

# ------------------------------- Imported Packages -------------------------------
from util import config as cfg
from util import start as strt
from util import import_data, calculation

# ---------------------------------- Main Program ---------------------------------

def main():

    end_program = False # variable used to check if user wants to exit program

    # loop until end_program is True
    while not end_program:

        # call menu function and get user's choice
        option = strt.menu()

        if option == 1: # import a x, y values from csv
            read_file = True
            file_path_error_message = ""
            import_file_message = "Importing your data via csv file"
            while read_file:    # loop when read_file is true
                cfg.clear_screen()
                print(f"You have chosen [{option}] {cfg.menu_options[option-1]}. \n")
                print("Please ensure your csv file is located in the 'data' folder. \nPress 'Enter' directly to use the default test data.")
                print(file_path_error_message)
                try:    # allow user to enter the file path
                    read_file_path = "data/" + input("Enter your file name (without .csv): \n") + ".csv"
                    if read_file_path == "data/.csv":   # check did user enter anything
                        read_file_path = cfg.default_read_file_path
                        import_file_message = "Importing default test data"
                    x_values, y_values = import_data.import_csv(read_file_path)  # call function
                    cfg.clear_screen()
                    print(import_file_message, "\n")
                    cfg.time_animation(3, "CSV file imported successfully. \n")
                    cfg.countdown(4)
                    read_file = False
                except FileNotFoundError:   # handle the error if an exception occurs, to prevent the program from being terminating
                    file_path_error_message = "\nNO SUCH FILE! REMEMBER TO LOCATE YOUR CSV FILE IN THE 'DATA' FOLDER. \n"

        elif option == 2: # calcuate and display the linear regression line
            cfg.clear_screen()
            print(f"You have chosen [{option}] {cfg.menu_options[option-1]}. \n")
            b_m = calculation.find_linear_regress(x_values, y_values)
            print("The y-intercept is", b_m[0])
            print("The gradient ", b_m[1])
            print(f"The least squares regression line of this set of data is approximately Y = {b_m[1]:.2f}x + {b_m[0]:.2f}")

        elif option == 3: # calcuate and display the correlation coefficient
            cfg.clear_screen()
            print(f"You have chosen [{option}] {cfg.menu_options[option-1]}. \n")
            print("option 3")

        elif option == 4: # plot scatter graph
            cfg.clear_screen()
            print(f"You have chosen [{option}] {cfg.menu_options[option-1]}. \n")
            print("option 4")

        else: # option 5 - exit in controlled manner

            end_program = True  # set end_program Boolean to True

            # output messages to user
            print("Thank you for using this program")
            print("Quitting Program...")

        #### END OF MAIN PROGRAM


if __name__ == "__main__":
    main()
