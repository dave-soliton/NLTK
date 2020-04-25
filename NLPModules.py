# Takes a file name and finds it in a directory,
# returning the path
def File_directory(file_name):
    import os 
  
    # This is to get the directory that the file resides in
    dir_path = os.path.dirname(os.path.realpath('/Users/Dave/Documents/CORD-19-research-challenge/')) 
  
    for root, dirs, files in os.walk(dir_path): 
        for file in files:  

            if file_name in file: 
#                print (root +'/'+str(file) )
                return root +'/'+str(file)



def Find_incubation(Abstract):
    from nltk.tokenize import PunktSentenceTokenizer
    # Instance of PunktSentenceTokenizer (pre learned)
    Token_abstract = PunktSentenceTokenizer()
    Token_lines = Token_abstract.tokenize(Abstract)
    for line in Token_lines:
        line = line.lower()
        if 'incubation period' in line:
#            print('Found it in:',line)
            return True
        
    return np.nan

# Subroutine to return True if string is True (not really needed)
def Covid(bol):
    
    if bol == True:
        return True   
    else:
        return False
    
class Country_tally:  
    def __init__(self, name, tally):  
        self.name = name  
        self.tally = tally
       
# Subroutine takes a dictionary of lists 'dict' and apends to the end all
# elements in dict2 not contained in dict, and appends to the elemets in 
# dict that are also in dict2
def check_country(dict, dict2): 
    for country, incubation in dict2.items():
        if country in dict: 
           #print(country + str(incubation) + 'is in')
           dict[country].append(incubation)
           #dict.setdefault(country, []).append(incubation)
        else: 
           #print(country + str(incubation) + 'is not in')
           dict.update({country:[incubation]})
           
    return dict
