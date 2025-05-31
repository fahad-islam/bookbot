from stats import get_num_words, get_num_characters

def main():
    num_words = get_num_words()
    char_counts = get_num_characters()

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    # Sort character counts and print them
    sorted_chars = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_chars:
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")
main()
