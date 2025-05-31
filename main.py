from stats import get_num_words, get_num_characters

def main():
    num_words = get_num_words()
    print(f"{num_words} words found in the document")
    print(get_num_characters())
main()
