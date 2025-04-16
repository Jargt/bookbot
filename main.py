def num_words(path):
    book = get_book_text(path)
    words = book.split()
    return len(words)


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    document = 'books/frankenstein.txt'
    print(f'{num_words(document)} words found in the document')

main()