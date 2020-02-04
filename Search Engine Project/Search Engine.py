from os import walk


SEPARATORS = (" ", "-")
REMOVABLES = (".", ",", ";", "(", ")")


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
    # Creates a list of all the file names in the specified folder,
    # then opens those files and put the name and data of those files in a dict
    for path, path_name, files in walk("Data"):
        for file_name in files:
            with open(".\\Data\\" + file_name) as file:
                file_data = file.read()
            data[file_name[:-4]] = file_data  # The [:-4] is to remove the .txt extension
    return data


def word_matcher(term, data: dict) -> list:
    results = []
    if type(term) == str:
        if term in data:
            for file_name in data:
                if term in file_name:
                    results.append(file_name)
        for file_name in data:
            for file_data in data[file_name]:
                if term in file_data:
                    results.append(file_name)
    elif type(term) == list:
        for word in term:
            if term in data:
                for file_name in data:
                    if term in file_name:
                        results.append(file_name)
            for file_name in data:
                for file_data in data[file_name]:
                    if term in file_data:
                        results.append(file_name)
    return results


def word_splitter(term: str) -> list:
    split_term = []
    for item in REMOVABLES:
        while item in term:
            item.replace(item, "")
    for item in SEPARATORS:
        if item in term:
            split_term = term.split(item)
    return split_term


term, result_count = inputs()
data = data_to_dictionary()
results = word_matcher(term, data)
term = word_splitter(term)
results = word_matcher(term, data)
