import sys
from stats import get_word_count, get_char_count, get_char_counts_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        book_text = get_book_text(path)
        num_words = get_word_count(book_text)
        char_counts = get_char_count(book_text)
        char_counts_list = get_char_counts_list(char_counts)
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f'Found {num_words} total words')
        print("--------- Character Count -------")
        for char_count in char_counts_list:
            print(f"{char_count['char']}: {char_count['num']}")
        print("============= END ===============")


if __name__ == "__main__":
  main()


