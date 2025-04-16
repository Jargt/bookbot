from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    document = 'books/frankenstein.txt'
    book_text = get_book_text(document)         #str
    num_words = get_num_words(book_text)        #int
    letters = get_letter_frequency(book_text)   #dict
    characters = sort_characters(letters)       #dict (sorted)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {document}...")
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    print("--------- Character Count -------")
    for character in characters:
        count = characters[character]
        print(f"{character}: {count}")
    print("============= END ===============")

main()