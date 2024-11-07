import sys
import os
import numpy as np

# Load the functions
def functionLoader():
    global EnergyDataset, HappinessIndex, CPI, UnploymentRate, HDI, Variable, AirPollutants, GDP, Utilities
    sys.path.append(sys.path[0] + "/..")
    import EnergyDataset, HappinessIndex, CPI, UnploymentRate, HDI, Variable, AirPollutants, GDP, Utilities

def topKCountriesList():
    return Utilities.extractTopKCountries(np.minimum(topKCountries, 30))

if __name__ == "__main__":
    functionLoader()
    EnergyDataset.mainPreparation()

    # Variables setup
    topKCountries, yearList = Variable.TOPKCOUNTRIES, Variable.YEARLIST
    country_list, iso_code_list = topKCountriesList()

    HappinessIndex.main(country_list, yearList)
    CPI.main(iso_code_list, yearList)
    UnploymentRate.main(iso_code_list, yearList)
    HDI.main(iso_code_list, yearList)
    AirPollutants.main(country_list, yearList)
    GDP.main(country_list, yearList)
    EnergyDataset.main(iso_code_list, yearList)