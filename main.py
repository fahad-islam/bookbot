from stats import get_num_words, get_num_characters
from sys import argv, exit

def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return exit(1)

    num_words = get_num_words(argv[1])
    char_counts = get_num_characters(argv[1])

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {argv[1]}...")
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
