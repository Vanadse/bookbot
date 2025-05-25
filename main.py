from stats import number_of_words_in #requires a string as an argument
from stats import number_of_characters_in # requires a string as an argument

# Returns a given file as a string ---------------
def get_book_text(path_to_book):
    with open(path_to_book) as f:
        return(f.read())
    

# Main starts here -------------------------------
def main():
    num_words = number_of_words_in(get_book_text("books/frankenstein.txt"))
    num_characters = number_of_characters_in(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")
    print(num_characters)

# Dont edit below here ---------------------------
main()
