import re
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def build_text_bank(url='http://www.politifact.com', stop_words=False):
    """
    Builds a hacky bank of politcs terms to use to filter text in the wild

    Parameters
    ==========
    page : page to scrape words from
    stopwords_csv : path to a csv called stopwords.csv with words you want to exclude

    Returns:
    ==========
    cleaned_words : all of the alphanumeric visable text found on the website
    """

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'xml')

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()
    text_tokenize = word_tokenize(text.replace('\n', ' ').replace('-', ' '))

    text_tokenize = word_tokenize(text_replace)
    text_tokenize = [t.lower() for t in text_tokenize]
    text_tokenize = [t for t in text_tokenize if not t.isdigit()]
    if stop_words:
        stopwords_ = set(stopwords.words('english'))
        cleaned_words = [t for t in text_tokenize if not t in stopwords_]
    else:
        cleaned_words = text_tokenize

    return cleaned_words


def filter_wild_text(sentence, text_bank):
    """
    Takes any english sentence in string form and extracts all words that are also in the textbank

    Parameters
    ==========
    sentence : any english sentence from a news article
    textbank : an array of words you want to filter for

    Returns:
    ==========
    new_bag : words in the sentence that are also in the textbank
    """

    bag_of_words = word_tokenize(sentence.replace('\n', ' ').replace('-', ' '))
    bag_of_words = [word.lower() for word in bag_of_words]
    bow_filter = []
    for word in bag_of_words:
        if "'s" in word:
            word = word.replace("'s'", "")
        bow_filter.append(word)
    bow_filter = list(filter(lambda x: x in text_bank, bow_filter))

    return bow_filter


if __name__ == "__main__":

    text_bank = build_text_bank(stopwords_csv=True) # make a bank of words using politifact's front bage
    raw_text = "17 years of interviews reveal trump's penchant for lewd talk" # Headline on cnn.com lol
    words_to_search = filter_wild_text(raw_text, text_bank)
    print(words_to_search)
