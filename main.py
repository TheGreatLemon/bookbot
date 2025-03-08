from stats import *

def get_book_text(file_handler):
    with open(file_handler) as f:
        return f.read()
    
    
def main():
    book_path = "books/frankenstein.txt"
    char_stats = sort_chars(get_char_counts(book_path))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(get_word_count(book_path))
    print("--------- Character Count -------")
    for i in range(0, len(char_stats)):
        print(f"{char_stats[i]["char"]}: {char_stats[i]["count"]}")
    
    
main()