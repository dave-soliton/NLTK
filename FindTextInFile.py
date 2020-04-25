# Quite naive, but returns the average number before 'word' (usually word = days)
def Number_before(word,Tokend_lines):
    number_list = []
    previous = next_ = ''
    l = len(Tokend_lines)
    for index, obj in enumerate(Tokend_lines):
        if obj == word:
            if index > 0:
                previous = Tokend_lines[index - 1]
            if index < (l - 1):
                next_ = Tokend_lines[index + 1]
    if previous.isdigit():
        number_list.append(int(previous))
        
    if len(number_list) < 1:
        return -1
    else:
        return sum(number_list) / len(number_list)
    
# Finds 'incubation period' a number and 'days' in a corpus
# and returns the lines concatenated that contains them
def Find_incubation_body(Abstract):
    from nltk.tokenize import PunktSentenceTokenizer
    from nltk.tokenize import word_tokenize
    import re
    incubation_text=''
    # Remove references from text '[number]'
    Abstract = re.sub(r" ?\[[^)]+\]", " ", Abstract)
    # Instance of PunktSentenceTokenizer (pre learned)
    Token_abstract = PunktSentenceTokenizer()
    Token_lines = Token_abstract.tokenize(Abstract)
    for line in Token_lines:
        # Converts line to lower case
        line = line.lower()
        if 'incubation' in line and 'days' in line:
            for s in line.split():
                # If has number in sentence 
                if s.isdigit():
                    incubation_text += line
 #                  print('Found it in:',line)
 #                  return True
        
    return incubation_text

def FindAveIncubationPeriodtInFile(FileId):
    #Finds sentences in a COVID-19 publication
    import NLPModules
    from nltk.tokenize import word_tokenize
    # Opens the json file found by File_directory
    import json
    FileId=str(FileId)
    file_dir=NLPModules.File_directory(FileId)
    if file_dir is not None:
        with open(file_dir, 'r') as j:
            json_data = json.load(j)
    else:
   #     print('Junk')
        return -1
    
    # Opens 'body_text' in json file and adds all of the
    # together
    Body_text=json_data.get("body_text")
    body_text =''
    for sentence in Body_text:
        body_text = body_text + sentence.get("text")
    # Search body_text for sentences containg incubation, day and number.
    # test_string is a conactanation of the sentences containing 'number' and
    # 'incubation period'
    test_string = Find_incubation_body(body_text)
    #print(test_string)
    
    # Finds numbers in 'test_string', first split sentence
    Token_lines = word_tokenize(test_string)
  
    # Returns a number found before 'days'
    #Prints average of number found before 'day'
 #   print('Average incubation: '+ str(Number_before('days',Token_lines)))
    
    return Number_before('days',Token_lines)