from stats import word_count, character_count, sort_result
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    #
    #print(character_count("sys.argv[1]"))
    print(f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------""")
    print(word_count(f"{sys.argv[1]}"))
    print("--------- Character Count -------")
    sort_result(character_count(f"{sys.argv[1]}"))
    print("============= END ===============")

main()