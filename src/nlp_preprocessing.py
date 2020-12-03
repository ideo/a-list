import gensim
from gensim.parsing.preprocessing import STOPWORDS
import pathlib

# TODO: get the hard coded path out of here.
def load_stopwords(stopwords_path = "../1_data/stopwords/"):
    p = pathlib.Path(stopwords_path)
    if not p.exists():
        print(f'Error {stopwords_path} not found')
        return

    stops = STOPWORDS
    for f in p.glob('*'):
        sw = f.open().read().split()
        stops = stops.union(set(sw))

    return stops

# def preprocess(text, stopwords):
#     tokens = gensim.utils.simple_preprocess(text,
#                                             deacc=True,
#                                             min_len=3,
#                                            )
#     tokens = [t for t in tokens if t not in stopwords]
#     return tokens