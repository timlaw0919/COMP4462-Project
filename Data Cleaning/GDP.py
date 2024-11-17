import sys
import pandas as pd

# Load the functions
def functionLoader():
    global LargeMain, Utilities, Variable
    sys.path.append(sys.path[0] + "/..")
    import LargeMain, Utilities, Variable

# Get the subset of data for the top k countries
def getSubsetData(country_list, dataList, year):

    data = dataList[0]

    present_countries = data['Country'].unique()
    missing_countries = [country for country in country_list if country not in present_countries]
    if missing_countries:
        print(f"GDP -> Missing countries in dataset: {missing_countries}")

    data.loc[:, 'GDP per Capita'] = data['GDP'] / data['Population']
    
    # print(data.columns)
    return data[(data['Country'].isin(country_list)) & (data['Year'] == year)][['Country', 'GDP', 'GDP per Capita']].assign(**{'Year': year})

# Main called by main.py to handle the data cleaning in the GDP Dataset
def main(country_list, yearList):
    functionLoader()

    dataFolderAbsolutePath, specific_file_name = Variable.ORIGINALDATAFOLDERPATH, Variable.GDPSPECIFICFILENAME
    data = Utilities.dataLoader(dataFolderAbsolutePath, specific_file_name)
    subset_data = []

    for i, year in enumerate(yearList):
        subset_data.append(getSubsetData(country_list, data, year))
        Utilities.storeDataInYears(subset_data[i][['Country', 'GDP', 'GDP per Capita']], "GDP", year)
    
    Utilities.storeDataInYears(pd.concat(subset_data), "GDP", '2015-2022')