def get_num_words(book):
    words = book.split()
    return len(words)

def get_letter_frequency(book):
    letter_dict = {}
    lower_case_book = book.lower() 
    for char in lower_case_book:
        if char in letter_dict:
            letter_dict[char] += 1
        else:
            letter_dict[char] = 1
    return letter_dict

def sort_characters(character_dict):
    sorted_dict = dict(sorted(character_dict.items(),reverse=True, key =lambda item:item[1]))
    return (sorted_dict)

def sort_on(dict):
    return dict['num']

