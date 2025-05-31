# Get book text
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    num_words = len(book_text.split())
    print(f"{num_words} words found in the document")

main()
