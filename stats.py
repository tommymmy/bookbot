def count_words(book):
    word_count = book.split()
    return word_count



def char_count(characters):
    frequency = {}
    chars = characters.lower()
    for c in chars:
        if c in frequency:
            frequency[c] += 1
        else:
            frequency[c] = 1
    return frequency

def dickt(d):
    new_list = []
    for key,value in d.items():
        if key.isalpha():
            new_list.append({"char": key, "num": value})
    return new_list

def sort_on(item): 
    return item["num"]

