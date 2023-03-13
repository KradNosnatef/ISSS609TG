import csv

with open("./assets/DisneylandReviews.csv","r",encoding="ISO-8859-1") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

# save each row of comments into seperate txt files with ReviewID as file names 
for row in reader:
    filename = f"./assets/row[0].txt"
    with open(filename, 'w') as f:
        
       f.write(str(row[4]))


import nltk, re
from nltk.corpus import PlaintextCorpusReader

def textfiles_to_tokens(folder, filename_pattern = '.+\.txt', verbose = False, 
                        return_corpus = False, use_recommended_tokenizer = False):
    corpus = PlaintextCorpusReader(folder, filename_pattern)
    cf = corpus.fileids()
    if use_recommended_tokenizer:
        tokens = [nltk.word_tokenize(corpus.raw(fid)) for fid in cf]
    else:
        tokens = [corpus.words(fid) for fid in cf]
    if verbose:
        x = re.findall(r'\w+$', folder)[0]
        print(f'Some sample {x} documents:')
        for i in cf[:5]: print(i)
        print(f'Some tokens in {x} document at index 0: \n', tokens[0][:20])
    if return_corpus:
        return tokens, corpus
    else:
        return tokens

import gensim
from gensim.parsing.porter import PorterStemmer
from gensim.models.phrases import Phrases, ENGLISH_CONNECTOR_WORDS

# Usual pre-processing for Stopwords, Alphabetic words and Stemming 
def preprocess_tokens(tokens, to_lower=True, only_alpha=True, stop_list=None, to_stem=True, to_lemmatize=False, 
                      min_len=1, bigrams_min_count=0, bigrams_threshold=1, bigram_model=None):
    all_docs2 = [[w.lower() for w in doc] for doc in tokens] if to_lower else tokens

    all_docs3 = [[w for w in doc if w.isalpha()] for doc in all_docs2] if only_alpha else all_docs2

    if stop_list is None:
        stop_list = gensim.parsing.preprocessing.STOPWORDS
    elif stop_list:
        stop_list = list(gensim.parsing.preprocessing.STOPWORDS) + stop_list
    else:
        stop_list = stop_list

    all_docs4 = [[w for w in doc if w not in stop_list and len(w) >= min_len] for doc in all_docs3]
    
    if to_stem:
        stemmer = PorterStemmer()
        all_docs5 = [[stemmer.stem(w) for w in doc] for doc in all_docs4]
    elif to_lemmatize:
        from nltk.stem import WordNetLemmatizer
        from nltk.corpus import wordnet
        try:
            tag_dict = wordnet.NOUN
        except LookupError:
            nltk.download('wordnet')
            nltk.download('omw-1.4')
        tag_dict = {'J': wordnet.ADJ, 'N': wordnet.NOUN, 'V': wordnet.VERB, 'R': wordnet.ADV}
        def get_wordnet_pos(word):
            """ Map POS tag to first character lemmatize() accepts"""
            tag = nltk.pos_tag([word])[0][1][0].upper()
            return tag_dict.get(tag, wordnet.NOUN)
        
        lemmatizer = WordNetLemmatizer()
        all_docs5 = [[lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in doc] for doc in all_docs4]
    else:
        all_docs5 = all_docs4

    if bigram_model is not None:
        return bigram_model[all_docs5]
    elif bigrams_min_count > 0:
        # non-zero bigrams_min_count to implement bigrams
        # the higher the bigrams_min_count and bigrams_threshold, the fewer bigrams will be formed
        bigram_model = Phrases(all_docs5, min_count=bigrams_min_count, threshold=bigrams_threshold, connector_words=ENGLISH_CONNECTOR_WORDS)
        return bigram_model[all_docs5], bigram_model
    else:
        return all_docs5


tokens = textfiles_to_tokens('assets')
docs = preprocess_tokens(tokens, to_stem = False, 
                           stop_list = ['would', 'said', 'say', 'year', 'day', 'also', 'first', 'last', 'one', 
                                        'two', 'people', 'told', 'new', 'could', 'singapore', 'three', 'may', 
                                        'like', 'world', 'since', 's', 't', 'm', 'mr'])