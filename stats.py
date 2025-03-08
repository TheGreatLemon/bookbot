def get_word_count(file_handler):
    text = ""
    with open(file_handler)as f:
        text = f.read()
    words = text.split()
    word_count = len(words)
    return f'{word_count} words found in the document'