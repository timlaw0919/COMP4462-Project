import sys

# Constants: Top k countries will be limited to maximum 30
TOPKCOUNTRIES = 30

# Constants: List of years
YEARLIST = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]

# Folder path for the data
HAPPINESSINDEXFOLDERPATH = sys.path[0] + "/../Original Data/D2_HappinessIndex"
ORIGINALDATAFOLDERPATH = sys.path[0] + "/../Original Data"
ENERGYCONSUMPTIONSPECIFICFILENAME = 'D1_EnergyConsumption.csv'
CPISPECIFICFILENAME = 'D3_AverageCPI.csv'
UNEMPLOYMENTSPECIFICFILENAME = 'D4_UnemployedRate.csv'
HDISPECIFICFILENAME = 'D5_HumanDevelopmentIndex.csv'
AIRPOLLUTANTSSPECIFICFILENAME = 'D6_AirPollutants.csv'
GDPSPECIFICFILENAME = 'D1_EnergyConsumption.csv'

CONCATFOLDERPATH = sys.path[0] + "/../Cleaned Data/2015-2022"

TASK4ENERGYDATA = ['CPI.csv', 'Unemployed Rate.csv', 'GDP.csv', 'Energy Consumption.csv']
TASK4HAPPINESSDATA = ['CPI.csv', 'Unemployed Rate.csv', 'GDP.csv', 'Happiness Index.csv']
TASK5ENERGYDATA = ['Human Development Index.csv', 'Energy Consumption.csv']
TASK5HAPPINESSDATA = ['Human Development Index.csv', 'Happiness Index.csv']