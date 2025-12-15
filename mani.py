import pandas as pd
# import numpy as np
import nltk
nltk.download('punkt_tab')
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()


music_file = pd.read_csv('spotify_data.csv')
# print(music_file.shape)
modified_file = music_file.drop(columns=['link']).reset_index(drop=True)
# print(modified_file.shape)
modified_file['text'] = modified_file['text'].str.lower().replace(r'^\w\s','').replace(r'\n,','', regex=True)

sample_with_1K = modified_file.sample(100)
# print(sample_with_1K.shape)

print(sample_with_1K.head(6))

def token(txt):
    token = nltk.word_tokenize(txt)
    a = [ps.stem(w) for w in token]
    print(a)
    return " ".join(a)

print(token("Loving the machine learning"))

sample_with_1K['text'].apply(lambda x: token(x))

tfid = TfidfVectorizer(analyzer='word',stop_words='english')
matrix = tfid.fit_transform(modified_file['text'])
similar_data = cosine_similarity(matrix)
print(music_file[music_file['song'] == 'Waiting for the Man'].index[0])

