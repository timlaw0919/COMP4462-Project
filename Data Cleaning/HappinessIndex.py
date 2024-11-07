import sys
import pandas as pd

# Load the functions
def functionLoader():
    global Utilities, LargeMain, Variable
    sys.path.append(sys.path[0] + "/..")
    import Utilities, LargeMain, Variable

# Get the subset of data for the top k countries
def getSubsetData(country_list, dataList):

    subset_data = []

    for index, data in enumerate(dataList):
        present_countries = data['Country'].unique()
        missing_countries = [country for country in country_list if country not in present_countries]
        if missing_countries:
            print(f"Happiness -> Missing countries in dataset {index + 2015}: {missing_countries}")
        
        subset_data.append(data[data['Country'].isin(country_list)][['Country', 'Happiness Score']].assign(**{'Year': index + 2015}))
    
    return subset_data

# Main called by main.py to handle the data cleaning in the Happiness Index Dataset
def main(country_list, yearList):
    functionLoader()

    dataFolderAbsolutePath = Variable.HAPPINESSINDEXFOLDERPATH
    data = Utilities.dataLoader(dataFolderAbsolutePath)
    subset_data = getSubsetData(country_list, data)
    
    for i, year in enumerate(yearList):
        Utilities.storeDataInYears(subset_data[i][['Country', 'Happiness Score']], "Happiness Index", year)
    
    Utilities.storeDataInYears(pd.concat(subset_data), "Happiness Index", '2015-2022')