# Returns a given file as a string ---------------
def get_book_text(path_to_book):
    with open(path_to_book) as f:
        return(f.read())
    
# Returns the number of words in a given string --
def number_of_words_in(given_string):
    count = 0
    for word in given_string.split():
        count += 1
    return(count)

# Main starts here -------------------------------
def main():
    num_words = number_of_words_in(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")

# Dont edit below here ---------------------------
main()
