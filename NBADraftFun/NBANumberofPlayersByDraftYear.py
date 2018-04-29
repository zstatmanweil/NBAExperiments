import json
import pandas as pd
import time

#npaplayers.json found here: http://data.nba.net/10s/prod/v1/2017/players.json
json_file = open ('nbaplayers.json')
json_str = json_file.read()
json_data = json.loads(json_str)

#accessing each player's dictionary
players = json_data['league']['standard']

#this function provides a table showing the number of players still active in
#2017 by the year they were drafted
def get_number_players():
    #creating set of draft_years and a list of players in each draft year
    draft_years = []
    draft_years_count = []
    
    #populating the set of draft years and list of players in each draft year
    for player in players:
        draft_year = player['draft']['seasonYear']
        
        if draft_year != '':
            draft_year = int(draft_year)
        else:
            draft_year = 0
        
        if draft_year not in draft_years:
            draft_years_count.append(1)
            draft_years.append(draft_year)
        else:
            i = list(draft_years).index(draft_year)
            draft_years_count[i] += 1     
    
    #creating and organizing data table
    data = {'No. of Players' : draft_years_count}
    sum_table = pd.DataFrame(data, draft_years)
    sum_table_sorted = sum_table.sort_index(ascending=True)
    sum_table_clean = sum_table_sorted.drop(0, axis=0)
    
    print """\nHere are the number of players still in the league \
from each draft year as of 2017. Note: \
there wasn't draft data for %d players. \n""" % sum_table_sorted.loc[0, "No. of Players"]
    
    time.sleep(1)
    print sum_table_clean