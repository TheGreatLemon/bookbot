def get_word_count(file_handler):
    text = ""
    with open(file_handler)as f:
        text = f.read()
    words = text.split()
    word_count = len(words)
    return f'Found {word_count} total words'

def get_char_counts(file_handler):
    text = ""
    char_counts = {}
    with open(file_handler) as f:
        text = f.read()
    for char in text:
        if char.isalpha(): 
            char = char.lower()
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts

def sort_on(dict):
    return dict["count"]

def sort_chars(char_dict):
    char_list = []
    for char in char_dict:
        char_list.append({"char": char, "count": char_dict[char]})
    char_list.sort(reverse=True, key = sort_on)
    return char_list