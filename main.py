from stats import number_of_words_in #requires a string as an argument
from stats import number_of_characters_in # requires a string as an argument
from stats import make_sorted_list_from # requires a dictionary as an argument

# Returns a given file as a string ---------------
def get_book_text(path_to_book):
    with open(path_to_book) as f:
        return(f.read())


# Main starts here -------------------------------
def main():
    book = "books/frankenstein.txt"
    num_words = number_of_words_in(get_book_text(book))
    num_characters = number_of_characters_in(get_book_text(book))
    #print(f"{num_words} words found in the document")
    #print(num_characters)
    #print(make_sorted_list_from(num_characters))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character in make_sorted_list_from(num_characters):
        char = character["char"]
        num = character["num"]
        print(f"{char}: {num}")
    print("============= END ===============")
# Dont edit below here ---------------------------
main()
