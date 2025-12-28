def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    
    return file_contents

def word_count(file):
    file_contents = get_book_text(file)
    
    word_list = file_contents.split()
    
    return f"Found {len(word_list)} total words"

def main():
    print(word_count("books/frankenstein.txt"))

main()