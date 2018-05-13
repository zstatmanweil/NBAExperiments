import json
import pandas as pd
import time

#npaplayers.json found here: http://data.nba.net/10s/prod/v1/2017/players.json
json_file = open (r'..\nbaplayers.json')
json_str = json_file.read()
json_data = json.loads(json_str)

#accessing each player's dictionary nad name
players = json_data['league']['standard']
        
#this function provides a list of NBA players still active in 2017 drafted 
#in a certain year
def get_players_names(year):
    #creating set of draft_years and a list of players in each draft year
    draft_years = []
    draft_years_names = []
    
    #populating the set of draft years and list of players in each draft year
    for player in players:
        draft_year = player['draft']['seasonYear']
        name = player['firstName'] + " " + player['lastName']
        
        if draft_year != '':
            draft_year = int(draft_year)
        else:
            draft_year = 0
        
        if draft_year not in draft_years:
            draft_years.append(draft_year)
            draft_years_names.append(name)
        else:
            i = draft_years.index(draft_year)
            draft_years_names[i] = draft_years_names[i] + ", " + name
        
    #creating and organizing data table
    data = {'Names of Players' : draft_years_names}
    sum_table = pd.DataFrame(data, draft_years)
    list_of_players = sum_table.loc[int(year), 'Names of Players']
    
    print """\nHere are are the NBA players drafted in %s that are still in \
the league: \n""" % (year)
    
    time.sleep(1)
    print list_of_players
    
#this function will get the draft year of a specific player
def get_draft_year_round(name):
    name_list = name.split(' ')
    firstname = name_list[0].lower()
    lastname = name_list[1].lower()

    i=0
    for player in players:
        player_fn = player['firstName'].lower()
        player_ln = player['lastName'].lower()
        
        if firstname == player_fn and lastname == player_ln:
            i = 1
            draft_year = player['draft']['seasonYear']
            draft_pick = player['draft']['pickNum']
            draft_round = player['draft']['roundNum']
            
            if draft_round == '1':
                draft_round = '1st'
            else:
                draft_round = '2nd'
            pass
        
        else:
            pass
        
        
    if i == 1 and draft_year != '':
        print """\n%s was drafted number %s in the %s round in %s""" % (name.title(), draft_pick, draft_round, draft_year)
    elif i == 1 and draft_year == '':
        print "\nThere is no draft data for %s, he may not have been drafted." % name.title()
    elif i != 1:
        print "\n%s wasn't active in the NBA in 2017." % name.title()
            