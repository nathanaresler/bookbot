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

def sort_on(items):
    return items["num"]

def sort_result(dict):
    character_list = []
    #convert dict to list of dictionarys to use .sort() method
    for item in dict:
        character_list.append({"character": item, "num": dict[item]})
    
    character_list.sort(reverse=True, key=sort_on)

    
    #print character and num of character list
    for i in character_list:
       if i["character"].isalpha():
           print(f"{i["character"]}: {i["num"]}") 