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

# Returns the value of "num" from a given dictionary
def sort_on(dict):
    return dict["num"]

# Returns a sorted list created from a given dictionary
def make_sorted_list_from(given_dictionary):
    sorted_list = []
    for character in given_dictionary:
        if character.isalpha():
            sorted_list.append({"char": character, "num": given_dictionary[character]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list