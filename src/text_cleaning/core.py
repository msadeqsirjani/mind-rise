import os
import re
import nltk
import string as st
import pandas as pd
import src.config as config
from nltk.corpus import stopwords
from nltk import PorterStemmer, WordNetLemmatizer

# nltk.download('stopwords')
# nltk.download('wordnet')

stop_words = stopwords.words('english')

path_csv = config.BASE_DIR + "/data/masters_portal.csv"
data_frame = pd.read_csv(path_csv)


def remove_punctuations(text):
    """
        Remove all punctuations from the text
    """
    if not isinstance(text, str):
        return text

    return "".join([ch for ch in text if ch not in st.punctuation])


def tokenize(text):
    """ Convert text to lower case tokens. Here, split() is applied on white-spaces. But, it could be applied
        on special characters, tabs or any other string based on which text is to be separated into tokens.
    """
    if not isinstance(text, str):
        return text

    return "".join([x.lower() for x in text])


def remove_small_words(text):
    """
        Remove tokens of length less than 3
    """
    if not isinstance(text, str):
        return text

    return "".join([x for x in text if len(x) > 3])


def remove_stopwords(text):
    """ Remove stopwords. Here, NLTK corpus list is used for a match. However,
        a customized user-defined list could be created and used to limit the matches in input text.
    """
    if not isinstance(text, str):
        return text

    return " ".join([word for word in text.split(' ') if word not in stop_words])


# Apply stemming to convert tokens to their root form. This is a rule-based process of word form conversion
# where word-suffixes are truncated irrespective of whether the root word is an actual word in the language dictionary.
# Note that this step is optional and depends on problem type.
def stemming(text):
    """
        Apply stemming to get root words
    """
    if not isinstance(text, str):
        return text

    ps = PorterStemmer()
    return "".join([ps.stem(word) for word in text])


# Lemmatization converts word to its dictionary base form. This process takes language grammar and vocabulary
# into consideration while conversion. Hence, it is different from Stemming in that it does not merely truncate the suffixes
# to get the root word.
def lemmatize(text):
    """
        Apply lemmatization on tokens
    """
    if not isinstance(text, str):
        return text

    word_net = WordNetLemmatizer()
    return "".join([word_net.lemmatize(word) for word in text])


def preprocess_pipeline(
        df,
        tokenize_flag=True,
        remove_punctuations_flag=True,
        remove_stop_words_flag=True,
        remove_small_words_flag=False,
        lemmatize_flag=True,
        stemmer_flag=True
):
    """
    input text
        ↳ [tokenize]
            ↳ [remove punctuations]
                ↳ [remove stop words]
                    ↳ [remove small words]
                        ↳ [lemmatize]
                            ↳ [stemmer]
                                ↳ output text
    """
    if tokenize_flag:
        df = df.apply(lambda x: tokenize(x))

    if remove_punctuations_flag:
        df = df.apply(lambda x: remove_punctuations(x))

    if remove_stop_words_flag:
        df = df.apply(lambda x: remove_stopwords(x))

    if remove_small_words_flag:
        df = df.apply(lambda x: remove_small_words(x))

    if lemmatize_flag:
        df = df.apply(lambda x: lemmatize(x))

    if stemmer_flag:
        df = df.apply(lambda x: stemming(x))

    return df


def pre_process(df: pd.DataFrame, persist: bool = False) -> pd.DataFrame:
    path = config.BASE_DIR + "/data/processed_portals.csv"
    if os.path.exists(path):
        df = pd.read_csv(path)

        return df

    df['extracted_keywords'] = ""

    for i in range(len(df)):
        processed_row = preprocess_pipeline(df=df.iloc[i])
        processed_row = processed_row.astype(str)
        df.at[i, 'extracted_keywords'] = ", ".join(processed_row.values)

    if persist:
        df.to_csv(path)

    return df
