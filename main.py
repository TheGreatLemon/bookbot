from stats import get_word_count

def get_book_text(file_handler):
    with open(file_handler) as f:
        return f.read()
    
    
def main():
    print(get_word_count("books/frankenstein.txt"))
    
    
main()