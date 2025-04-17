from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    document = sys.argv[1] 
    book_text = get_book_text(document)         #str
    num_words = get_num_words(book_text)        #int
    letters = get_letter_frequency(book_text)   #dict of letters and counts
    sorted_list = sort_characters(letters)       #list of dicts (sorted)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {document}...")
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    print("--------- Character Count -------")
    for items in sorted_list:
        print(f"{items['char']}: {items['num']}")
    print("============= END ===============")

main()