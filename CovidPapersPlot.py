# Generates Histogram of when COVID-19 relervant papers were published

def CovidPublishedHistogram(Med_data_Virus):
    import pandas as pd

    # Pass one to Covid_papers if a paper was published in that date
    # used for plotting of dates.
    Med_data_Virus['Covid_papers']=Med_data_Virus['Covid'].map(counting)
    Med_data_Virus['Covid_papers'] = Med_data_Virus['Covid_papers'].fillna(0)
    
    # Convert publish_time to date format
    Med_data_Virus['publish_date'] =pd.to_datetime(Med_data_Virus['publish_time'])
    
    # Remove all colums but publish_date and Covid_papers
    Med_data_Virus=Med_data_Virus[['publish_date','Covid_papers']]
    
    # Remove NANs
    Med_data_Virus=Med_data_Virus.dropna()
    
    # Plot histogram of dates
    (Med_data_Virus.loc[Med_data_Virus['publish_date'].dt.year.between(2018, 2020), 'publish_date']
             .dt.to_period('M')
             .value_counts()
             .sort_index()
             .plot(kind="bar")
    )
    
# Return int(1) if bol = True
def counting(bol):
    import numpy as np
    if bol == True:
        return int(1)   
    else:
        return np.nan
