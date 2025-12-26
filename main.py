import sys
from stats import number_of_words, character_count, sort_char_counts

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

def get_book_text(path):
    with open(path) as file:
        text = file.read()
    return text


def main():
    book_text = get_book_text(path)
    num_words = number_of_words(book_text)
    char_counts = character_count(book_text)
    sorted_chars = sort_char_counts(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}") 


main()