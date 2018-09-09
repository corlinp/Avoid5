from thesaurus import Word
import re

common = {
    'the': 'that', 
    'they': 'those', 
    'me': 'myself',
}

def has5(word):
    for glyph in word:
        if glyph.lower() == 'e':
            return True
    return False

def find_synonym(word):
    if word in common:
        return common[word]
    w = Word(word)
    syns = w.synonyms()
    for syn in syns:
        if not has5(syn):
            return syn
    return word.replace('e', '-')

def fix(text):
    s = text.split(' ')
    for i in range(len(s)):
        if has5(s[i]):
            word = re.sub('[^a-z]+', '', s[i].lower())
            s[i] = find_synonym(word)
    return " ".join(s)

text = input("Input words with dirty glyphs: ")

print(fix(text))