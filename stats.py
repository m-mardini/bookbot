#!/usr/bin/env python3

def get_book_text(filepath):
    print(f"Analyzing book found at {filepath}...")
    with open(filepath) as f:
        contents = f.read()
    return contents

def count_words(book_text):
    print("----------- Word Count -----------")
    answer = len(book_text.split())
    print(f"Found {answer} total words")
    return answer

def count_characters(book_text):
    answer = {'a': 0}
    for char in book_text:
        if char.lower() in answer.keys():
            answer[char.lower()] += 1
        else:
            answer[char.lower()] = 1
    return answer

def sort_character_list(character_dict):
    print("---------- Character Count ----------")
    answer = []
    for char, count in character_dict.items():
        answer.append({"char": char, "num": count})
    def sort_on(dict):
        return dict["num"]
    answer.sort(reverse=True, key=sort_on)
    for d in answer:
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["num"]}")
    return answer
