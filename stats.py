def number_of_words(text):
    words = text.split()
    return len(words)


def character_count(text):
    lower_text = text.lower()
    char_counts = {}
    for char in lower_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts


def sort_on_num(item):
    return item["num"]


def sort_char_counts(char_counts):
    chars_list = []
    for ch in char_counts:
        char_dict = {"char": ch, "num": char_counts[ch]}
        chars_list.append(char_dict)
    chars_list.sort(key=sort_on_num, reverse=True)
    return chars_list
