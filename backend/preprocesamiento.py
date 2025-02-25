import json
from ntpath import join
import os
from turtle import down
from nltk.stem import SnowballStemmer
import re
import nltk
from nltk import word_tokenize


def generateStopFile(file):
    with(open(file, "r", encoding="utf-8") as file):
        stop_list = [line.lower().strip()  for line in file]
    return stop_list

def clean(text):
    text = re.sub("@[A-Za-z0-9_]+", " ", text)
    text = re.sub("#[A-Za-z0-9_]+", " ", text)
    text = re.sub(r'http\S+', ' ', text)
    text = re.sub('[()!?]', ' ', text)
    text = re.sub('\[.*?\]', ' ', text)
    text = re.sub("[^áéíóú+a-z0-9]", " ", text)
    text = re.sub('\\b[^y0-9]{1} \\b', ' ', text)
    return text


def generateTokens(text, stop_words):
    tokens, tokens_return = [], []
    text = clean(text.strip().lower())
    text = nltk.word_tokenize(text)
    tokens = [w for w in text if not w in stop_words]
    stemmer = SnowballStemmer('spanish')
    for token in tokens:
        tokens_return.append(stemmer.stem(token))
    return tokens_return


def generateTokensOfFiles(data_path, stop_words):
    data_files = os.listdir(data_path)
    tokens_tweets = []
    tokens_file = []
    for file in data_files:
        decode_file = open(join(data_path, file), "r", encoding="utf-8")
        tweets = json.load(decode_file)
        for tweet_text in tweets:
            text = tweet_text['text']
            tokens_tweet = generateTokens(text, stop_words)
            tokens_tweets.extend(list(dict.fromkeys(tokens_tweet)))
        tokens_tweets = list(dict.fromkeys(tokens_tweets))
        tokens_file.append(tokens_tweets)
        tokens_tweets = []
        print("end" + file)
    return tokens_file


text = "suuuuuuu..  @Renzo_Reggiardo me da mala espina...su pasado fujimorísta qué miedo!!!y @luchocastanedap hijo de corrupto que secunda lo del padre NI HABLAR! Más comunicore Plop!lideran las preferencias para la alcaldía de Lima, según Ipsos | RPP Noticias https://t.co/w5TnU0Dmwq"
print(generateTokens(text, generateStopFile("stoplist.txt")))

text = text.lower()
text = re.sub("@[A-Za-z0-9_]+", " ", text)
text = re.sub("#[A-Za-z0-9_]+", " ", text)
text = re.sub(r'http\S+', ' ', text)
text = re.sub('[()!?]', ' ', text)
text = re.sub('\[.*?\]', ' ', text)
text = re.sub("[^áéíóú+a-z0-9]", " ", text)
text = re.sub('\\b[^y0-9]{1} \\b', ' ', text)
text = word_tokenize(text)
stemmer = SnowballStemmer('spanish')
tokens = []
stop_words = generateStopFile("stoplist.txt")
text = [w for w in text if not w in stop_words]
for token in text:
    tokens.append(stemmer.stem(token))

print(tokens)
