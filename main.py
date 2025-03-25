from stats import get_num_words
from stats import get_num_characters
from stats import prepare_characters_list
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()

    return  file_content

def main():
    args = sys.argv

    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = args[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found {file_path}")
    print("----------- Word Count ----------")
    book_text = get_book_text(file_path)
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    characters = get_num_characters(book_text)
    sorted_list = prepare_characters_list(characters)

    for item in sorted_list:
        name = item["name"]
        value = item["num"]
        if not name.isalpha():
            continue
        print(f"{name}: {value}")

    return None

main()
