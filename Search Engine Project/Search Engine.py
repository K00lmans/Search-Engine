def inputs() -> [str, int]:
    term = input("Please enter your search term: ")
    while True:
        try:
            result_count = int(input("How many results would you like to find: "))
            break
        except:
            print("Please enter a number")
    return(term, result_count)


print(inputs())
