from stats import get_word_count, get_char_counts

def get_book_text(file_handler):
    with open(file_handler) as f:
        return f.read()
    
    
def main():
    print(get_word_count("books/frankenstein.txt"))
    char_stats = get_char_counts("books/frankenstein.txt")
    print(char_stats)
    
    
main()