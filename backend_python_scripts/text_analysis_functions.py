
import urllib2
from bs4 import BeautifulSoup
import csv
import re




def scrape_frontpage_terms(page='http://www.politifact.com',stopwords_csv=None):

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

    stopwords = [] # OK if empty
    if stopwords_csv:
        with open(stopwords_csv, 'rb') as csvfile:
            reader = csv.reader(csvfile,delimiter='\n')
            for row in reader:
                stopwords.append(row[0])

    req = urllib2.Request(page)

    response = urllib2.urlopen(req)
    page_content = response.read()
    soup = BeautifulSoup(page_content,'xml')

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = [chunk.split() for chunk in chunks if chunk]

    cleaned_words = []
    for words in text:
        for word in words:
            word = word.lower()
            word = filter(lambda x: x.isalnum(),word)
            if word not in stopwords:
                cleaned_words.append(word)

    return cleaned_words


def filter_wild_text(sentence,textbank):

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

    bag_of_words = sentence.split(" ")
    bag_of_words = [word.lower() for word in bag_of_words]
    new_bag = []
    for word in bag_of_words:
        if "'s" in word:
            word = word[:word.index("'s")]
        new_bag.append(word)
    new_bag = filter(lambda x: x in textbank, new_bag)

    return new_bag


if __name__ == "__main__":

    #change me to run
    REPO_DIR = '/Users/Torben/Documents/politicrowd_factcheck/'
    stopwords_csv=REPO_DIR+'stopwords.csv'

    #make a bank of words using politifact's front bage
    text_bank = scrape_frontpage_terms(stopwords_csv=stopwords_csv)

    #Headline on cnn.com lol
    raw_text = "17 years of interviews reveal trump's penchant for lewd talk"


    words_to_search = filter_wild_text(raw_text,text_bank)
    print words_to_search


