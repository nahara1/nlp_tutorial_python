'''
Intro to NLP Tutorial @
https://towardsdatascience.com/gentle-start-to-natural-language-processing-using-python-6e46c07addf3
This module prompts the user for a url and language of a web page,
clean html tags, remove stop words, and then outputs the frequency
of each word in the text found in the given web page.
'''

import nltk
import urllib.request

# run this command on the terminal:
# pip install beautifulsoup4 - Python library to scrape web pages

from bs4 import BeautifulSoup
from nltk.corpus import stopwords

page_url = input("Enter URL: ")
page_language = input("Enter language: ")

response = urllib.request.urlopen(page_url)
html = response.read()
print(html)
soup = BeautifulSoup(html, 'html5lib')
text = soup.get_text(strip=True)
print(text)

# create a list of all the words found in the web page
tokens = [t for t in text.split()]
print(tokens)

sr = stopwords.words(page_language)
clean_tokens = tokens[:]

# remove all stop words
for token in tokens:
    if token in stopwords.words(page_language):
        clean_tokens.remove(token)

# FreqDist is called to count word frequency
freq = nltk.FreqDist(clean_tokens)

for key, val in freq.items():
    print(str(key) + ':' + str(val))
freq.plot(20, cumulative=False)
