def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin reports of {book_path} --- ")
    text = get_book_text(book_path)
    chars_dict = count_char(text)
    chars_sorted = chars_dict_to_sorted(chars_dict)
    #print(text)
    #print(f"Total line:{count_line(text)} line")
    print(f"{count_line(text)} words found in the document")
    for item in chars_sorted:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def sort_on(dict) :
    return dict["num"]

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_line(string) :
    return len(string.split())

def chars_dict_to_sorted(chars_dict):
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({"char": char, "num": chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def count_char(string) :
    char_count = {}
    for char in string :
        if char.lower() in char_count :
            char_count[char.lower()] += 1
        else :
            char_count[char.lower()] = 1
    return char_count

main()
