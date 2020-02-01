import os


def inputs() -> [str, int]:
    """Takes the constraints from the user for the search"""
    term = input("Please enter your search term: ")
    # Asks for the number of results the the user would like to see, and makes sure it is an int
    while True:
        try:
            result_count = int(input("How many results would you like to find: "))
            break
        except ValueError:
            print("Please enter only a whole number")
    return term, result_count


def data_to_dictionary() -> dict:
    """Turns the raw data in the text files into a dict"""
    data = {}
    # Creates a list(?) of all the file names in the specified folder,
    # then opens those files and put the name and data of those files in a dict
    for root, dirs, files in os.walk("Data"):
        for file_name in files:
            with open(".\\Data\\" + file_name) as file:
                file_data = file.read()
            data[file_name[:-4]] = file_data  # The [:-4] is to remove the .txt extension
    return data


term, result_count = inputs()
data = data_to_dictionary()
