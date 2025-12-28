def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    
    return file_contents

def word_count(file):
    
    file_contents = get_book_text(file)
    
    word_list = file_contents.split()
    
    return f"Found {len(word_list)} total words"

def character_count(file):

    file_contents = get_book_text(file).lower()
    character_count = {}
    for character in file_contents:
        if character not in character_count:
            character_count[character] = 1
        else:
            character_count[character] += 1
    
    return character_count