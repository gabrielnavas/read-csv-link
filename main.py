import pandas as pd

# read csv from web link

# url files: https://www.football-data.co.uk/englandm.php

# get data
data_csv = pd.read_csv('https://www.football-data.co.uk/mmz4281/2223/E0.csv')

#rename columns
data_csv.rename({ 
    'FTHG': 'home_goals', 
    'FTAG': 'away_goals', 
})