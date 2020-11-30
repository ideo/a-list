import gensim
from gensim.parsing.preprocessing import STOPWORDS

# TODO: get the hard coded path out of here.
def load_stopwords(stopwords_path = "../1_data/stopwords/stopwords.txt"):
    with open(stopwords_path, "r") as f:
        sw = f.read().split()
    return STOPWORDS.union(set(sw))

# def preprocess(text, stopwords):
#     tokens = gensim.utils.simple_preprocess(text,
#                                             deacc=True,
#                                             min_len=3,
#                                            )
#     tokens = [t for t in tokens if t not in stopwords]
#     return tokens