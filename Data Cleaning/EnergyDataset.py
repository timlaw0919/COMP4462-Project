import sys
import pandas as pd

# Load the functions
def functionLoader():
    global LargeMain, Utilities, Variable
    sys.path.append(sys.path[0] + "/..")
    import LargeMain, Utilities, Variable

# Get the subset of data for the top k countries
def getSubsetData(iso_code_list, dataList, year):

    data = dataList[0]
    present_countries = data['iso_code'].unique()
    missing_countries = [code for code in iso_code_list if code not in present_countries]
    if missing_countries:
        print(f"Human Development Index -> Missing countries in dataset {missing_countries}")

    return data[(data['iso_code'].isin(iso_code_list)) & (data['Year'] == year)].drop(columns=['GDP', 'iso_code', 'population'])

# Missing values handling
def missingValuesHandling(data):
    data = data.fillna(0)
    return data

# Prepration for the main.py
def mainPreparation():
    global data
    functionLoader()

# Main called by main.py to handle the data cleaning in the Energy Dataset
def main(iso_code_list, yearList):
    functionLoader()

    # Variables setup
    dataFolderAbsolutePath, specific_file_name = Variable.ORIGINALDATAFOLDERPATH, Variable.ENERGYCONSUMPTIONSPECIFICFILENAME
    data = Utilities.dataLoader(dataFolderAbsolutePath, specific_file_name)
    subset_data = []

    for i, year in enumerate(yearList):
        subset_data.append(getSubsetData(iso_code_list, data, year))
        Utilities.storeDataInYears(missingValuesHandling(subset_data[i].drop(columns = ['Year'])), "Energy Consumption", year)
    
    Utilities.storeDataInYears(missingValuesHandling(pd.concat(subset_data)), "Energy Consumption", '2015-2022')

# # Testing purposes
# if __name__ == "__main__":
#     functionLoader()
#     data = Utilities.dataLoader(dataFolderAbsolutePath)
#     country_list, iso_code_list = extractTopKCountries(data, main.topKCountries)