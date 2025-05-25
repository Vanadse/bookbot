# Returns the number of words in a given string --
def number_of_words_in(given_string):
    count = 0
    for word in given_string.split():
        count += 1
    return(count)