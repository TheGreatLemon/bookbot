def get_word_count(file_handler):
    text = ""
    with open(file_handler)as f:
        text = f.read()
    words = text.split()
    word_count = len(words)
    return f'{word_count} words found in the document'

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