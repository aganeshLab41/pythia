from bs4 import BeautifulSoup
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
import re


def text_to_words(raw_text):
    '''
    Algorithm to convert raw text to a return a clean text string
    Method modified from code available at:
    https://www.kaggle.com/c/word2vec-nlp-tutorial/details/part-1-for-beginners-bag-of-words
    Args:
        raw_text: Original text to clean and normalize
    Returns:
        clean_text: Cleaned text
    '''
    # 1. Remove web links
    links_removed = re.sub(r'\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', raw_text)
    #
    # 2. Remove HTML   
    #TODO Potentially look into using package other than BeautifulSoup for this step
    review_text = BeautifulSoup(links_removed, "lxml").get_text()
    #
    # 3. Remove non-letters 
    letters_only = re.sub("[^a-zA-Z]", " ", review_text)
    #
    # 4. Convert to lower case, split into individual words
    words = letters_only.lower().split()
    #
    # 5. Remove stop words
    meaningful_words = [w for w in words if not w in ENGLISH_STOP_WORDS]
    #
    # 6. Join the words back into one string separated by space,
    # and return the result.
    clean_text = ( " ".join( meaningful_words ))
    return   clean_text