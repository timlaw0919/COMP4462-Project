import sys
import pandas as pd

# Load the functions
def functionLoader():
    global Utilities, LargeMain, Variable
    sys.path.append(sys.path[0] + "/..")
    import Utilities, LargeMain, Variable

# Get the subset of data for the top k countries
def getSubsetData(country_list, dataList, year):

    data = dataList[0]

    for index, data in enumerate(dataList):
        present_countries = data['Country'].unique()
        missing_countries = [country for country in country_list if country not in present_countries]
        if missing_countries:
            print(f"Air Pollutants -> Missing countries in dataset: {missing_countries}")
        
    subset = data[(data['Country'].isin(country_list)) & (data['Year'] == year)].copy()
    numeric_columns = subset.select_dtypes(include=['number']).columns
    subset.loc[ : , 'Total Air Pollutants'] = subset[numeric_columns].sum(axis = 1)
    subset = subset.assign(Year = year)

    return subset

# Main called by main.py to handle the data cleaning in the Happiness Index Dataset
def main(country_list, yearList):
    functionLoader()

    dataFolderAbsolutePath, specific_file_name = Variable.ORIGINALDATAFOLDERPATH, Variable.AIRPOLLUTANTSSPECIFICFILENAME
    data = Utilities.dataLoader(dataFolderAbsolutePath, specific_file_name)
    subset_data = []

    for i, year in enumerate(yearList):
        subset_data.append(getSubsetData(country_list, data, year))
        Utilities.storeDataInYears(subset_data[i][['Country', 'Nitrogen Oxide', 'Sulphur Dioxide', 'Carbon Monoxide', 'Organic Carbon', 'NMVOCs', 'Black Carbon', 'Ammonia', 'Total Air Pollutants']], "Air Pollutants", year)
    
    Utilities.storeDataInYears(pd.concat(subset_data), "Air Pollutants", '2015-2022')