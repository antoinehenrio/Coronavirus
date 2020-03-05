import urllib
import urllib2
import bs4 as BeautifulSoup
from urllib2 import urlopen
# from urllib.request import urlopen
import datetime
import csv
import pandas as pd
from Tkinter import *

date = datetime.datetime.now()
fichiers = []
url = 'https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports'
fichier = urlopen(url)
soup = BeautifulSoup.BeautifulSoup(fichier,'html.parser')
soup.prettify()
css_soup = soup.find_all("tr","js-navigation-item")
tables = soup.find_all('tr')
for table in css_soup:
    fichiers.append(table.a.get_text())
taille = len(fichiers) - 2
fichierActuel = fichiers[taille]
i = 0
compteurMorts = 0
urlfinal = url + "/" + fichierActuel
data = []
mon_fichier = urllib2.urlopen(urlfinal)
soupCsv = BeautifulSoup.BeautifulSoup(mon_fichier,'html.parser')
soupCsv.prettify()
lignes = soupCsv.find_all("tr", id=lambda value: value and value.startswith("LC"))
for ligne in lignes:
    mots = ligne.find_all('td')
    for mot in mots:
        if i == 5:
            compteurMorts = compteurMorts + int(mot.get_text())
        i = i + 1
    i = 0
# print('Nombre de morts {}'.format(compteurMorts))

fenetre = Tk()
champ_label = Label(fenetre, text="Nombre de morts : {}".format(compteurMorts))
champ_label.pack()
fenetre.mainloop()
