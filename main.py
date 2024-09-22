def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_character_count(text):
    char_count = {}
    for char in text:
        lower_char = char.lower()
        if lower_char not in char_count and lower_char.isalpha():
            char_count[lower_char] = 1
        elif lower_char.isalpha():
            char_count[lower_char] += 1
    char_count_list = []
    for char in char_count:
        char_count_list.append({"char": char, "num": char_count[char]})
    char_count_list.sort(reverse=True, key=sort_on)
    return char_count_list

def sort_on(dict):
    return dict["num"]

def get_word_count(text):
    return len(text.split())

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    word_count = get_word_count(text)
    char_count = get_character_count(text)
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in document\n")
    for char in char_count:
        print(f"The '{char["char"]}' character was found {char["num"]} times")
    print("--- End report ---")
main()