from stats import num_words
from stats import char_count

def get_book_text(file_path):
    with open(file_path) as f:
        # f is a file object
        file_contents = f.read()
        #print(file_contents)
        
    return file_contents

#def num_words(txt):
#    numberofwords = len(txt.split())
#    return numberofwords


def main():
    #print("1")
    filecontents = get_book_text("books/frankenstein.txt")

    countedwords = num_words(filecontents)
    freq = char_count(filecontents)
    

    print(countedwords, "words found in the document")
    print(freq)


    #print("2")
    #print(filecontents)
    #print("3")

main()