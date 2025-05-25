# Returns the number of words in a given string -----------------------------------
def number_of_words_in(given_string):
    count = 0
    for word in given_string.split():
        count += 1
    return(count)

# Returns the amount of each type of character, including spaces, in a given string
def number_of_characters_in(given_string):
    characters = {}
    for character in given_string.lower():
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1
    return characters