import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        pass
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    words = count_words(text)
    total_words = len(words)
    output_word_count = f"Found {total_words} total words"
    characters = list(text)
    characters_string = " ".join(characters)
    word_count_dict = char_count(text)
    new_dict = dickt(word_count_dict)
    new_dict.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at: {book_path}")
    print("----------- Word Count ----------")
    print(output_word_count)
    print("--------- Character Count -------")
    for item in new_dict:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

    

def get_book_text(path):
    with open(path) as f:
        return f.read()

from stats import count_words

from stats import char_count

from stats import dickt

from stats import sort_on

main()
