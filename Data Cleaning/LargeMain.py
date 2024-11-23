import sys
import os
import numpy as np

# Load the functions
def functionLoader():
    global EnergyDataset, HappinessIndex, CPI, UnploymentRate, HDI, Variable, AirPollutants, GDP, Utilities, DataConcat, AirQuality
    sys.path.append(sys.path[0] + "/..")
    import EnergyDataset, HappinessIndex, CPI, UnploymentRate, HDI, Variable, AirPollutants, GDP, Utilities, DataConcat, AirQuality

def topKCountriesList():
    return Utilities.extractTopKCountries(np.minimum(topKCountries, 100))

if __name__ == "__main__":
    functionLoader()
    EnergyDataset.mainPreparation()

    # Variables setup
    topKCountries, yearList = Variable.TOPKCOUNTRIES, Variable.YEARLIST
    country_list, iso_code_list = topKCountriesList()

    # HappinessIndex.main(country_list, yearList)
    CPI.main(iso_code_list, yearList)
    UnploymentRate.main(iso_code_list, yearList)
    HDI.main(iso_code_list, yearList)
    AirPollutants.main(country_list, yearList)
    GDP.main(country_list, yearList)
    EnergyDataset.main(iso_code_list, yearList)
    AirQuality.main(country_list, yearList)
    HappinessIndex.main(country_list, yearList)

    # Concatenate the data
    DataConcat.main("Task 1", Variable.TASK1DATA)
    DataConcat.main("Task 4 Energy Data", Variable.TASK4ENERGYDATA)
    DataConcat.main("Task 4 Happiness Data", Variable.TASK4HAPPINESSDATA)
    DataConcat.main("Task 5 Energy Data", Variable.TASK5ENERGYDATA)
    DataConcat.main("Task 5 Happiness Data", Variable.TASK5HAPPINESSDATA)