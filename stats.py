def get_num_words(text):
    return len(text.split())

def get_num_characters(text):
    char_list = {}

    for char in text:
        c = char.lower()
        if not (c in char_list):
            char_list[c] = 0
        char_list[c] += 1

    return char_list

def prepare_characters_list(characters):
    list = []

    for c in characters:
        list.append({"name": c, "num": characters[c]})
    return sorted(list, key=lambda item: item["num"], reverse=True)
