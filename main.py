from stats import get_num_words
from stats import get_total_l
from stats import sortd
from stats import h
import sys
def main():
    path = sys.argv
    this = 0
    for i in path:
        this += 1
        if this == 2:
          book = i  
    if this < 2:
        print("Usage: python3 main.py <path_to_book>(.. means previous folder, . means this folder.)")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book)} total words")
    print("--------- Character Count -------")
    x = get_total_l(book)
    v = sortd(x)
    v.sort(key=h, reverse=True)
    for di in v:
        print(f"{di["char"]}: {di["num"]}")
    print("============= END ===============")
main()