from os import walk


SEPARATORS = (" ", "-")
REMOVABLES = (".", ",", ";", "(", ")", "[", "]", "{", "}")


def inputs() -> [str, int]:
    """Takes the constraints from the user for the search"""
    term = input("Please enter your search term: ").lower()
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


def word_matcher(term, data: dict, results: list, result_count: int) -> list:
    """Main search loop"""
    # If there is only one term, look through it once
    if type(term) == str:
        for data_item in data:
            # If the term is in one of the titles, add to results
            if term in data_item.lower() and data_item not in results:
                results.append(data_item)
        if result_count > len(results):
            for data_item in data:
                # If the term is in content of a document, and the document has not already been added, add to results
                if term in data[data_item].lower() and data_item not in results:
                    results.append(data_item)
    elif type(term) == list:
        for each_term in term:
            for data_item in data:
                # If the term is in one of the titles, add to results
                if each_term in data_item.lower() and data_item not in results:
                        results.append(data_item)
            for data_item in data:
                # If the term is in content of a document, and the document has not already been added, add to results
                if each_term in data[data_item].lower() and data_item not in results:
                    results.append(data_item)
    # Should never run
    else:
        print("Something went very wrong, please restart.")
        while True:
            pass
    return results


def word_splitter(term: str):
    """Splits the term"""
    # Removes items that may clog the search
    for item in REMOVABLES:
        while item in term:
            term = term.replace(item, "")
    # If there are things that separates words in the term, separate them
    for item in SEPARATORS:
        if item in term:
            term = term.split(item)
    if type(term) == list:
        for item in term:
            if item == "":
                term.remove(item)
    return term


results = []
term, result_count = inputs()
data = data_to_dictionary()
results = word_matcher(term, data, results, result_count)
# Only does secondary check if max results has not been found
if len(results) < result_count:
    term = word_splitter(term)
    new_results = word_matcher(term, data, results, result_count)
print(results)
