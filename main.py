#!/usr/bin/python3

import sys
from stats import get_num_words, get_num_char, sorted_dicts


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")

    text = get_book_text(path)
    num_words = get_num_words(text)

    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for d in sorted_dicts(get_num_char(text)):
        print(f"{d["char"]}: {d["num"]}")

    print("============= END ===============")


main()