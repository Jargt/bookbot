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
    character_list = []
    for character in character_dict:
        little_dict = {
            'char': character,
            'num': character_dict[character],
        }
        character_list.append(little_dict)
    character_list.sort(reverse = True, key = sort_on)
    return (character_list)

def sort_on(dict):
    return dict['num']

