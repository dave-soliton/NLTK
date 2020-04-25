import pandas as pd
import numpy as np
from geotext import GeoText
import matplotlib.pyplot as plt
import NLPModules
import CovidPapersPlot
import Plot

# Import csv file
Med_data_uncleaned=pd.read_csv('/Users/Dave/Documents/CORD-19-research-challenge/metadata.csv',low_memory=False)


# Pass imported DataFrame to a second one, for faster prototyping
Med_data=Med_data_uncleaned



# Searching for COVID in DataFrame, creating two more columns  
Med_data["Covid_abs"]= Med_data["abstract"].str.contains('Covid-19|covid-19|COVID|COVID-19|Novel Coronavirus|novel coronavirus|SARS-CoV-2') 
Med_data["Covid_title"]= Med_data["title"].str.contains('Covid-19|covid-19|COVID|COVID-19|Novel Coronavirus|novel coronavirus|SARS-CoV-2') 

# Make Covid_abs and Covid_title have True or False
Med_data['Covid_abs']=Med_data['Covid_abs'].map(NLPModules.Covid)
Med_data['Covid_title']=Med_data['Covid_title'].map(NLPModules.Covid)

# Covid now shows if 'Covid' is in either the title or the abstract,
# to remove non Covid papers.
Med_data['Covid'] = np.logical_or(Med_data['Covid_abs'] == True,Med_data['Covid_title']== True)

# Reset the DataFrame index and remove the old one.
Med_data=Med_data.reset_index()
Med_data_Virus=Med_data.drop(['index'],axis = 1)

# DataFrame containing COVID related papers
Covid_Data=Med_data.drop(['index'],axis = 1)
Covid_only_data=Covid_Data[Covid_Data['Covid']]
# Plots a histogram of Covid-19 paper occurences
CovidPapersPlot.CovidPublishedHistogram(Med_data_Virus)



# As a prototype look for 'incubation period' in title or abstract
Med_data["Covid_incubation_in_abs"]= Covid_Data["abstract"].str.contains('incubation|gestation')

# Remove NANs.
Incubation_data=Med_data
Incubation_data=Incubation_data.dropna(subset=['Covid_incubation_in_abs'])
Incubation_data=Incubation_data[Incubation_data['Covid_incubation_in_abs']]

# As a prototype look for 'incubation period' in title or abstract
Incubation_data["Inc_abs"]= Incubation_data["abstract"].str.contains('incubation period')
Incubation_data=Incubation_data[Incubation_data['Inc_abs']]

# Prototype: Populates Has_Covid_Incubation_period if has in in abstract
Incubation_data['Has_Covid_Incubation_period']=Incubation_data['abstract'].map(NLPModules.Find_incubation)
Incubation_data=Incubation_data.dropna(subset=['Has_Covid_Incubation_period'])

# Opens the json file found by File_directory
import FindTextInFile

Covid_only_data=Covid_only_data.dropna(subset=['sha'])
# Reset the DataFrame index and remove the old one.
Covid_only_data=Covid_only_data.reset_index()
Covid_only_data=Covid_only_data.drop(['index'],axis = 1)

Incubation_period_list =[]
i=0
import Country_incubation
# fileOfInterest = Covid_only_data.sha[466] This has and average of 20!
# for paper in Covid_only_data.sha:
#     #fileOfInterest = Covid_only_data.sha[466]
#     fileOfInterest = paper
#     print(i)
#     i+=1
#     if fileOfInterest is not None:
#         Incubation_period=FindTextInFile.FindAveIncubationPeriodtInFile(fileOfInterest)
#         if Incubation_period >0 and Incubation_period <100:
#             Incubation_period_list.append(Incubation_period)
#     else:
#         print('rubish' + str(paper))
i=0
country_incubation_dict = {}
country_incubation_dict_tmp = {}  
for paper in Covid_only_data.sha:
    sha = paper
    country_incubation_dict_tmp=Country_incubation.country_incubation(Covid_only_data.title[i],Covid_only_data.abstract[i],sha)
    i+=1
    if len(country_incubation_dict_tmp)>0:
        #print('New list')
        #print(country_incubation_dict_tmp)
        country_incubation_dict=NLPModules.check_country(country_incubation_dict, country_incubation_dict_tmp) 
        print('Updated list')
        print(country_incubation_dict)
        
Plot.Plot_country_incubation(country_incubation_dict)
       
plt.figure(figsize=(25, 15))
plt.plot(Incubation_period_list)
plt.show()
# Need to combine the above functions to read the corpus of the texts and return the relervant numbers, then do this for the counties relervent texts.


# Concatanates abstracts to find list of counties
text2 = str(Med_data.abstract[0])
for word in Med_data.abstract:
    text2 = text2 + str(word)



# Finds list of countries 'country_occurence'
places = GeoText(text2)
country_occurence=places.country_mentions



# Removes countries which are mentiond less then 50 times
countries=[]
for key, value in country_occurence.items():
    if value > 50:
        countries.append([key, value])



# Plots country occurnces
x = np.linspace(0, 2, 100)

x, y = zip(*countries) # unpack a list of pairs into two tuples
plt.figure(figsize=(25, 15))
plt.bar(x, y)

plt.title("Occurance by country")

plt.show()


# Adds abstracts together for WORD cloud
i=0
for word in Med_data['abstract']:
    places2 = GeoText(str(word))
    country_occurencees = places2.country_mentions
    if len(country_occurencees) > 0:
        gg=word
        break

import WordCloud
# make a word cloud
#WordCloud.WordCloud_Image(text2)







