def If_there(text):
#Daft, but removes crazy space formatting
    text_list = text.split()
    for word in text_list:
        text +=" "+word
        
    look='cat sat'
    
    if look in text:
        print('cat')
        
If_there('The cat \n         sat on the matt')