from stats import word_count, character_count, sort_result

def main():
    #
    #print(character_count("books/frankenstein.txt"))
    print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------""")
    print(word_count("books/frankenstein.txt"))
    print("--------- Character Count -------")
    sort_result(character_count("books/frankenstein.txt"))
    print("============= END ===============")

main()