import pandas
import numpy
import math
import os
import re
from nltk.tokenize import RegexpTokenizer

#sastrawi
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

file_data = open('./Data/Air Panas Banjar.csv')

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
        #         lower_word = data[['objek','ulasan','label']][line].lower() #test gagal
        lower_word = line, data['objek'][line], data['ulasan'][line].lower(), data['label'][line]
        remove_punctuation = stopword.remove(lower_word)
        arr_praproses.append([remove_punctuation])

    #         print(" ")# coba print
    #         print(lower_word)# coba print
    return arr_praproses


Pra_Proses(data)
# a