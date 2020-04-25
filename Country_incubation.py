# Does Abstract, or tile, mention a country
# if so is there an 'incubation period' in the body?

def country_incubation(title,abstract,sha):
    from geotext import GeoText
    import FindTextInFile
    
    text = str(title) + str(abstract)
    places = GeoText(text)
    country_occurence=places.country_mentions
    country_incubation_dct={}
    incubation_period=FindTextInFile.FindAveIncubationPeriodtInFile(sha)
    if incubation_period >0 and len(country_occurence)>0 and incubation_period <50:
        country_list=[*country_occurence.keys()]
        #print('Has an incubation period of '+str(incubation_period))
        country_incubation_dct = {country_list[i]: incubation_period for i in range(0, len(country_list))}
        
    return country_incubation_dct

