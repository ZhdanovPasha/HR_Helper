import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer 
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import sent_tokenize


def text_preprocessing(text):
    tokens = word_tokenize(text)
    table = str.maketrans('', '', string.punctuation)
    tokens = [w.translate(table) for w in tokens]
    tokens = [word.lower() for word in tokens]
    tokens = [word for word in tokens if word.isalpha()]
    stop_words = set(stopwords.words('russian'))
    tokens = [word for word in tokens if not word in stop_words]
    return ' '.join(tokens)

def convert_parsed_item_to_string(value, join_symbol='. '):
    if not value:
        return ''
    if type(value) == str:
        return value
    elif type(value) == list:
        if type(value[0]) == str:
            return value[0]
        else:
            return join_symbol.join(list(value[0].values()))
        
def join_text_from_json_by_values(mapping, join_symbol=' '):
    return join_symbol.join(
        [convert_parsed_item_to_string(value) for value in mapping.values()]
    )