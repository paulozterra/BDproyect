import params
from cleaner import clean
from preprocesamiento import generateStopFile


def preapp_static():
    #cleaning static data
    clean(params.static_path_folder, params.static_clean_path)

    #generate stopwords
    stop_words = generateStopFile(params.stoplist_file)

    #create_invertindex and saving

    #calculate norma of ever file

    #saving invertindex
    # SAVE INVERTINDEX BLOCKS IN INDICE BLOCKS

    # MERGE BLOCKS


def consult_static(query, topk):

    # convert query to tokens
    # search tokens in indicesdb
    # get score and text

    #create dic of score[N] ; N = total tweets
    #use dic of Norms[N]
    #for each t in query_terms
    #   calculate Wt,qry
    #   for each doc of t that is in index_inverted
    #       do  score[doc] += Wt,qry * Wt,doc
    #for each doc in Norms
    #   do Scores[doc] = Scores[doc]/Norms[doc]
    #sort Scores
    #return TopK

    # return topk score and text

    return topk


#Indice INVERTIDO ESCALABLE

# ORDENAR EN FUNCION DE TERMINOS

preapp_static()