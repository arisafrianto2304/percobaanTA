from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.tokenize import RegexpTokenizer
import pandas as pd
import numpy as np
import math
import os
import re
 
def combine_data(filename=None, ulasan=None, output_path=None):
    df = pd.read_csv(filename, encoding = "ISO-8859-1")

    du = pd.DataFrame(data=ulasan, columns=["ulasan"])
    df = df[["objek", "ulasan", "label"]]

    df[["ulasan"]] = du
    # untuk save dataframe ke file
    df.to_csv(output_path)
    
    return df

def preprocessing(input_path=None): #, stopword=stopword, stemmer=stemmer):
    factori = StemmerFactory()
    stemmer = factori.create_stemmer()

    factory = StopWordRemoverFactory()
    stopword = factory.create_stop_word_remover()

    tokenizer = RegexpTokenizer(r'\w+')

    arr_praproses = list()
    with open (input_path, 'r',  encoding='"ISO-8859-1"') as input :
        reader = input.read().split("\n")               #Akses data per baris
        for indeks in range(len(reader)):
            lowcase_word = reader[indeks].lower()       #case folding lowcase data perbaris
            stopw = stopword.remove(lowcase_word)       #uncomment jika pakai stopword removal
            stemming = stemmer.stem(stopw)              #uncomment jika pakai stemming
            tokens = tokenizer.tokenize(stemming)       #Tokenisasi Kalimat, tergantung proses terakhirnya, stemming atau stopword atau hanya casefolding
            output = list()       
            for kata in tokens:
                output.append(kata)                     #proses stemming per-kata dalam 1 kalimat
            sentence = " ".join(output) + ''
            arr_praproses.append(sentence)                #tampung kalimat hasil stemm ke arr_praproses
    
    return arr_praproses

fileall = 'Data/dataset.csv'
ulasan  = 'Data/ulasan.csv'
list_ulasan = preprocessing(input_path=ulasan)
clean_data  = combine_data(filename=fileall, ulasan=list_ulasan, output_path='Data/clean_data.csv')

print(clean_data)

'''
def Load_Data(input_file): 
    data = pandas.read_csv(input_file)
    data = pandas.DataFrame(data[['objek','ulasan','label']])
    return data

# data = Load_Data(file_data)
# data.head()

factori = StemmerFactory()
stemmer = factori.create_stemmer()

factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()

tokenizer = RegexpTokenizer(r'\w+')
data = Load_Data(file_data)


def Pra_Proses(data):
    arr_praproses = []
    for line in range(len(data)):
        print(line)
        #         lower_word = data[['objek','ulasan','label']][line].lower() #test gagal
        lower_word = line, data['objek'][line], data['ulasan'][line].lower(), data['label'][line]
        remove_punctuation = stopword.remove(lower_word)
        arr_praproses.append([remove_punctuation])

    #         print(" ")# coba print
    #         print(lower_word)# coba print
    return arr_praproses


Pra_Proses(data)
# a
'''