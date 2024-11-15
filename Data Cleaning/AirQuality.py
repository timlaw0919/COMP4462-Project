import sys
import pandas as pd

# Load the functions
def functionLoader():
    global Utilities, LargeMain, Variable
    sys.path.append(sys.path[0] + "/..")
    import Utilities, LargeMain, Variable

def getSubsetData(country_list, dataList, year):
    # Assume dataList is a list of DataFrames
    data = dataList[0]

    data = data.fillna(0)
    
    # Check if the 'version' column exists
    if 'version' in data.columns:
        # Filter rows where the 'version' starts with 'V6.0'
        data = data[data['version'].str.strip().str.startswith('V6.0', na=False)]
    
    # Proceed with your existing logic
    for index, data in enumerate(dataList):
        present_countries = data['Country'].unique()
        missing_countries = [country for country in country_list if country not in present_countries]
        if missing_countries:
            print(f"Air Quality -> Missing countries in dataset: {missing_countries}")
        
    # Subset data based on country list and specific year
    subset = data[(data['Country'].isin(country_list)) & (data['Year'] == year)].copy()
    subset = subset.drop(columns = ['Year'])
    subset = subset[['Country', 'pm10_concentration', 'pm25_concentration', 'no2_concentration']]
    
    # Calculate the total air pollutants concentration
    numeric_columns = subset.select_dtypes(include=['number']).columns
    subset.loc[:, 'Total Air Pollutants Concentration'] = subset[numeric_columns].sum(axis=1)
    
    subset = subset.groupby('Country', as_index = False).sum()
    
    # Add the year column back to the DataFrame
    subset = subset.assign(Year=year)

    return subset

# Main called by main.py to handle the data cleaning in the Happiness Index Dataset
def main(country_list, yearList):
    functionLoader()

    dataFolderAbsolutePath, specific_file_name = Variable.ORIGINALDATAFOLDERPATH, Variable.AIRQUALITYSPECIFICFILENAME
    data = Utilities.dataLoader(dataFolderAbsolutePath, specific_file_name)
    subset_data = []

    for i, year in enumerate(yearList):
        subset_data.append(getSubsetData(country_list, data, year))
        Utilities.storeDataInYears(subset_data[i][['Country', 'pm10_concentration', 'pm25_concentration', 'no2_concentration', 'Total Air Pollutants Concentration']], "Air Quality", year)
    
    Utilities.storeDataInYears(pd.concat(subset_data), "Air Quality", '2015-2022')