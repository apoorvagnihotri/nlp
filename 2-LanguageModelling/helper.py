import nltk
import re
nltk.download('punkt')

# some perticulat functions
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

# get tokenized sentences present in "filename"
def getSents(filename):
    # reading the file and using word_tokenize
    f = open(filename, 'r', encoding="utf8")
    raw = f.read()
    f.close()
    
    """
    remove 1 new line as the dataset has useless
    new lines for no reason, well, for better
    readibility. Anyways.

    will replace a single \n with a space.
    """
    line = re.sub(r"\n(\n*)", "\1", raw)
    return sent_tokenize(raw)

"""
brief:
Run a word tokenizer on the sentences generated and 
remove any nonaplabetical words. Furter lower the
cases in each word.

params:
takes in a list of list of strings.
"""
def lowerPunct(sentences):
    r =[]
    for sentence in sentences:
        list_words = word_tokenize(sentence)
        r.append([word.lower() for word in \
                  list_words if word.isalpha()])
    return r

"""
Add start and stop symbols to a given set of
sentences.
"""
def addStartStop(sentences):
    r =[]
    for sentence in sentences:
        l = ['<s>']
        l.extend(sentence)
        l.append('</s>')
        r.append(l)
    return r

'''
gives out a dictionary that has a structure
similar to a trie.
'''
def nGramCount(sentences, count = 3):
    dic = {}
    for i in range (1, count + 1):
        for sentence in sentences:
            state = []
            for word in sentence:
                state.append(word)
                if len(state) > i:
                    state.pop(0)
                if len(state) == i:
                    # add ngram to the dictionary.

def increaseCountDictionary(dic, ngram):
    try:
        for word in ngram:
            if ngram[0] == word:
                dicr =
            dic = dic[word]


