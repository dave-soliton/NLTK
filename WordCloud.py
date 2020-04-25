def WordCloud_Image(text2):
    # Import Word cloud
    from wordcloud import WordCloud, STOPWORDS
    import matplotlib.pyplot as plt
    
    
    # Remove stop words and some other common words
    stopwords = set(STOPWORDS)
    stopwords.update(["found","suggest","present", "abstract", "use", "based","associated","system","data","among", "one","may","results","many","method","change","known","two","well","showed","CONCLUSIONS","addition","three","either","Although","result","effect","group","show","BACKGROUND","thu","method","different","compared","including","identified","conclusion","within","used","using"])
    
    
    
    
    # Make Word Cloud
    wordcloud = WordCloud(width = 800, height = 800, 
                    background_color ='white',
                    stopwords = stopwords, 
                    min_font_size = 10).generate(text2)
    
    
    
    # Plot Word Cloud
    plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 
    plt.show()