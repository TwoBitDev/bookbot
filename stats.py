def num_words(txt):
    numberofwords = len(txt.split())
    return numberofwords

def char_count(txt):
    characterdictionary = txt.lower()
    freq = {}
    for c in set(characterdictionary):
        freq[c] = characterdictionary.count(c)
    return freq