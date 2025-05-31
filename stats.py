path_to_file = "./books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_num_words():
    book_text = get_book_text(path_to_file)
    return len(book_text.split())

def get_num_characters():
    book_text_character = list(get_book_text(path_to_file).lower())
    book_characters_dict = {}

    for character in book_text_character:
        if character in book_characters_dict:
            book_characters_dict[character] = book_characters_dict[character] + 1
        else:
            book_characters_dict[character] = 1
    return book_characters_dict
