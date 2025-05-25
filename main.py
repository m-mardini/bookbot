#!/usr/bin/env python3
from stats import get_book_text, count_words, count_characters, sort_character_list
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    character_count = count_characters(book_text)
    sorted_characters = sort_character_list(character_count)

main()
