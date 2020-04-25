def Plot_country_incubation(raw_data):
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    # Data
    # r = [0,1,2,3,4]
    # raw_data = {'PFHxA': [5, 4, 3,2, 1], \
    #         'PFHpA': [5, 15, 5, 10, 15], \
    #         'PFOA': [2, 15, 18, 5, 10], \
    #         'PFNA': [2, 15, 18, 5, 10], \
    #         'PFDA': [2, 15, 18, 5, 10], \
    #         'PFUnDA': [2, 15, 18, 5, 10], \
    #         'PFHxS': [2, 15, 18, 5, 10], \
    #         'PFOS': [2, 15, 18, 5, 10]}
    
        # Plots country occurnces
    x = np.linspace(0, 2, 100)
    
    
    plt.figure(figsize=(25, 15))
    for data, values in raw_data.items():
        lst = values
        lst.sort(reverse = True)
        print(lst)
        for i in lst:
            x = data
            y = i # unpack a list of pairs into two tuples
            plt.bar(x, y)
    
    plt.title("Occurance by country")
    
    
    # Custom x axis
    plt.xlabel("Countries")
    
    # Custom y axis
    plt.ylabel("Incubation periods")
    
    
    # Show graphic
    plt.show()