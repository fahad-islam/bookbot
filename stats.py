
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_num_words():
    book_text = get_book_text("./books/frankenstein.txt")
    return len(book_text.split())
