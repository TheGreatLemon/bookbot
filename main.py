def get_book_text(file_handler):
    with open(file_handler) as f:
        return f.read()
    
def get_word_count(file_handler):
    text = ""
    with open(file_handler)as f:
        text = f.read()
    words = text.split()
    word_count = len(words)
    return f'{word_count} words found in the document'
    
    
def main():
    print(get_word_count("books/frankenstein.txt"))
    
    
main()