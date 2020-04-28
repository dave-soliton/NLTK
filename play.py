import re
def If_there(text):
#Remove carrage return and excessive white space
    text = re.sub('\n', ' ', text)
    text = re.sub(' +', ' ', text)
        
    look='cat sat'
    
    if look in text:
        print('cat')

If_there('the cat \n  sat house')

import pandas as pd 
  
def Dicts(top):
    dts = {'Sales':0,'Revenue':top}
    return dts

# initialize list of lists 
data = [['tom', 10], ['nick', 15], ['juli', 14]] 
  
# Create the pandas DataFrame 
df = pd.DataFrame(data, columns = ['Name', 'Age']) 
df['DDts']=df['Age'].map(Dicts)

# print dataframe. 
print(df)

print(df['DDts'][0]['Revenue'])