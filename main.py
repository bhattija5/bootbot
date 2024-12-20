import collections #Used for Counter
#Reads the given textfile
def main():
    book_path = "books/frankenstein.txt"
    text = read_text(book_path)
    num_words = words(text)
    char_dict = count(text)
    chars_sorted_list = chars_dict_to_sorted_list(char_dict)
   
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def read_text(path):
    with open(path) as f:
        return f.read()
    
 #Prints out the number of words inside of the given text file   
def words(text):
    lines = text.split()
    return len(lines)

def count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

main()
