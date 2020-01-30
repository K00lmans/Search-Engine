import os


def inputs() -> [str, int]:
    term = input("Please enter your search term: ")
    while True:
        try:
            result_count = int(input("How many results would you like to find: "))
            break
        except:
            print("Please enter a number")
    return(term, result_count)


def data_to_dictionary() -> dict:
    data = {}
    # I do not know how this code segment works.
    for root, dirs, files in os.walk("Data"):
        for filename in files:
            data[filename[:-4]] = "data"
