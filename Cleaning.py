import csv
import nltk
from nltk.corpus import stopwords
import nltk.collocations
import collections
import re, string
import pandas
from emails import *
import datetime
from dateutil.parser import *
from TextUtils import *
#dt = parser.parse("Aug 28 1999 12:00AM")


def remove_punctuation ( text ):
    return re.sub('[%s]' % re.escape(string.punctuation), ' ', text)

"""
training_info_sid_min.csv C'est un fichier qui est un extrait du fichier training_info_sid.csv
On l'a fait pour minimiser les temps du execution
"""
f = open('./Datasets/training_info_sid_min.csv', 'r')
reader = csv.reader(f, delimiter=',', quotechar='"')
steamer = Steamer()


"""
On mettre le text brut du fichier CSV (colonne 2) dans une list (body_list)
"""
id_list = []
date_list = []


body_list = []
destinataires_list = []
expediteurs_list = []
for row in reader:
    id_list.append(row[0])
    date_list.append(row[1])
    body_list.append(row[2])
    destinataires_list.append(row[3])
    #expediteurs_list.append(row[4])

#(DATE)
"""
year
month
days
isoweekday()
"""
year_date_list = []
month_date_list = []
day_date_list = []
weekday_date_list = []
for i in range(0,len(date_list)):
    dt = parse(date_list[i])
    year_date_list.append(dt.year)
    month_date_list.append(dt.month)
    day_date_list.append(dt.day)
    weekday_date_list.append(dt.isoweekday())


"""
On nettoie le text brut pour simplifier le utilisation de l'algorithme de Machine Learning (après)
la sortie c'est une liste de mots en minuscule sans les stopwords
"""
body_clean_list = []
for email in body_list:
    email = remove_punctuation(email)
    body_clean_list.append([str.lower(word) for word in str.split(email) if (str.lower(word) not in stopwords.words('english'))])

email_list = []    
print(len(id_list))
print(len(date_list))
print(len(body_list))
print(len(destinataires_list))
print(len(id_list)-len(date_list))
for i in range(0,len(id_list)):
    email_list.append(Email(id_list[i], date_list[i], body_list[i], destinataires_list[i],""))
    # print("############## ID_LIST ##############")
    # print(id_list[i])  
    # print("############## BODY_LIST ##############")
    # print(body_list[i])
    # print("############## DATE_LIST ##############")
    # print(date_list[i])
    # print("############## DESTINATAIRES_LIST ##############")
    # print(destinataires_list[i])
"""
for i in range(0,len(id_list)):
    email_list.append(Email(id_list[i], date_list[i], body_clean_list[i], destinataires_list[i],""))
    print(body_clean_list[i])
    print("##############") 
"""

    
for email in email_list:
    email['text'] = steamer.clean(email['text'])
    email['tokenise'] = steamer.removeStopWords(this.tokenise(email['text']))
    print(email['tokenise'])
    print("#############################")

    
"""    
pd = pandas.DataFrame(id_list, date_list, destinataires_list, body_clean_list)
pd.to_csv("out.csv")
"""


        
    
    
    
    
    
    
    
