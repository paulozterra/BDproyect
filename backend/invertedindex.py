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
        
        #se crea la carpeta 
        #se guardan los diccionarios en archivos de la carpeta
        
        # for files in carpeta
        # open file[i]
        # open file[i+1]
        # open filetemp
        
            # for j in range file 
                # temp1=file[i]word[j]
                # temp2=file[i+1]word[j]

                # se crea otro doc donde se pondra el ID-termino

                # if temp1 != temp2
                    # id[temp1] = i
                    # id[temp2] = i + 1
                    # Agregar el temp1 y temp2 al filetemp si aun no existen 
                    # for id in IDS: 
                        # if id = i :
                        # filetemp[id][2]// acceder al diccionario xd //.push_back(file[i]word[j][2] // diccionario de docs)  // agrengando los docs a cada termino
                        # se deberia agregar solo a los docs que no estan presentes 

                # else 
                # id[temp1] = i
                # Agregar el temp1 al filetemp si aun no existe
                # comparar temp1.diccionario con temp2.diccionario  
                # for a in temp1.diccionario.size()
                    # if temp1.diccionario[a] != temp2.diccionario[a] and document is not in filetemp[id][2]
                        # filetemp[id][2].push_back(documento) 


            # tengo sueño quizas se me paso algo xd
            #  guardar el filetemp 
        
        
        
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

