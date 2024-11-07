import os
import pandas as pd
import sys

# Load the functions
def functionLoader():
    global Variable
    sys.path.append(sys.path[0] + "/..")
    import Variable

# Function to load data from a folder and return a list of dataframes
def dataLoader(folder_path, specific_file_name = None):

    data = []

    for file_name in os.listdir(folder_path):
        if specific_file_name is not None and file_name != specific_file_name:
            continue
        else:
            file_path = os.path.join(folder_path, file_name)
            try:
                df = pd.read_csv(file_path)
                data.append(df)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

    return data

# Extract the top k countries with the highest GDP in 2022
def extractTopKCountries(k):
    functionLoader()
    data = dataLoader(Variable.ORIGINALDATAFOLDERPATH, Variable.ENERGYCONSUMPTIONSPECIFICFILENAME)
    top_k = data[0][(data[0]['Year'] == 2022) & (data[0]['Country'] != 'World')].nlargest(k, 'GDP')[['iso_code', 'Country']]
    country_list = top_k['Country'].tolist()
    iso_code_list = top_k['iso_code'].tolist()
    return country_list, iso_code_list

# Store the data in different years in a folder
def storeDataInYears(df, df_name, year):
    os.makedirs(sys.path[0] + f"/../Cleaned Data/{year}", exist_ok = True)
    df.to_csv(sys.path[0] + f"/../Cleaned Data/{year}/{df_name}.csv", index = False)