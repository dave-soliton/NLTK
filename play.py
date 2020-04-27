import re
def If_there(text):
#Remove carrage return and excessive white space
    text = re.sub('\n', ' ', text)
    text = re.sub(' +', ' ', text)
        
    look='cat sat'
    
    if look in text:
        print('cat')

If_there('the cat \n  sat house')