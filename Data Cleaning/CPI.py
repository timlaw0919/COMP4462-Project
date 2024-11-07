import sys
import pandas as pd

# Load the functions
def functionLoader():
    global Utilities, LargeMain, Variable
    sys.path.append(sys.path[0] + "/..")
    import Utilities, LargeMain, Variable

# Get the subset of data for the top k countries
def getSubsetData(iso_code_list, dataList, year):

    data = dataList[0]

    present_countries = data['Country Code'].unique()
    missing_countries = [code for code in iso_code_list if code not in present_countries]
    if missing_countries:
        print(f"CPI -> Missing countries in dataset {missing_countries}")
    
    return data[data['Country Code'].isin(iso_code_list)][['Country']].assign(**{'CPI': data[str(year)], 'Year': year})

# Main called by main.py to handle the data cleaning in the CPI Dataset
def main(iso_code_list, yearList):
    functionLoader()

    # Variables setup
    dataFolderAbsolutePath, specific_file_name = Variable.ORIGINALDATAFOLDERPATH, Variable.CPISPECIFICFILENAME
    data = Utilities.dataLoader(dataFolderAbsolutePath, specific_file_name)
    subset_data = []

    for i, year in enumerate(yearList):
        subset_data.append(getSubsetData(iso_code_list, data, year))
        Utilities.storeDataInYears(subset_data[i][['Country', 'CPI']], "CPI", year)
    
    Utilities.storeDataInYears(pd.concat(subset_data), "CPI", '2015-2022')