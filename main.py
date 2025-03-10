from stats import *
import sys

def get_book_text(file_handler):
    with open(file_handler) as f:
        return f.read()
    
    
def main():
    params = sys.argv
    if len(params) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = params[1]
    char_stats = sort_chars(get_char_counts(book_path))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(get_word_count(book_path))
    print("--------- Character Count -------")
    for i in range(0, len(char_stats)):
        print(f"{char_stats[i]["char"]}: {char_stats[i]["count"]}")
    
    
main()