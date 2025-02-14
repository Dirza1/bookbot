def main ():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        characters = character_count(file_contents)
        report = generate_report(characters)
        #print (characters)

def count_words (book):
    words = book.split()
    count = len(words)
    return count

def character_count (book):
    characters = {    }
    text = book.lower()

    for x in text:
        if x in characters:
            characters[x] +=1
        else:
            characters[x] = 1
    return (characters)

def generate_report(book):
    
    list_of_duictionaries = [{"character":k, "frequencie" : v} for k, v in book.items()]
    list_of_duictionaries.sort(reverse=True, key=sort_on)
    for x in list_of_duictionaries:
        if x["character"].isalpha() == True:
            print(f"The '{x["character"]}' character was found {x["frequencie"]} times")

def sort_on(dict):
    return dict["frequencie"]

    
main()