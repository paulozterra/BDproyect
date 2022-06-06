import json
import os
import math
import re
import time
from ntpath import join
from preprocesamiento import generateTokens
from memoriasec import saveIndex
from memoriasec import readIndex


def generateIndexInv(tokens, data_path, stop_words):
    data_files = os.listdir(data_path)
    index_inv = {}
    for token in tokens:
        index_inv[token] = [0, {}]
    num_tweets = 0
    for file in data_files:
        # MODIFY WITH BLOCKS in secondary MEMORY
        # CREATE A BLOCK TO EACH FILE 
        # OR TO EACH X FILES 
        # OR WHEN YOUR INDEX_INV HAVE A X LIMIT
        # X IS PROPOSED BY US
        decode_file = open(join(data_path, file), "r", encoding="utf-8")
        tweets = json.load(decode_file)
        num_tweets += len(tweets)
        for tweet in tweets:
            text = tweet['text']
            text = text.generateTokens(text, stop_words)
            for word in text:
                if tweet['id'] in index_inv[word][1]:
                    index_inv[word][1][tweet['id']] += 1
                else:
                    index_inv[word][1][tweet['id']] = 1
                    index_inv[word][0] += 1
        decode_file.close()
    return [index_inv, num_tweets]

/*
- Apartir de "N" bloques realizamos un tipo de diccionario term - documento id 
- apartir de este diccionario vamos a tener term ID( a cada termino se le asigna un id para guardar menos bytes) y documentos ID
- leemos de dos en dos bloques y comparamos los termID (juntamos los documentos ID segun cada term ID)
- Juntamos en otro bloque y luego lo guardamos (repetir el mismo proceso hasta tener un solo bloque)

*/
