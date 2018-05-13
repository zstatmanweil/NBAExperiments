import pandas as pd
import time
from Player import Player
from Choice import Choice
import sys

class Application(object):
    def __init__(self, raw_data):
        self.players = self.convert_to_players(raw_data)

#converts players created from the Player class into a list of players
    def convert_to_players(self, raw_data):
        players = []
        for player in raw_data:
            player = Player(
                    player['firstName'],
                    player['lastName'],
                    player['draft']['seasonYear'],
                    player['draft']['pickNum'],
                    player['draft']['roundNum']
                    )
            players.append(player)
        return players

#starts the application
    def run(self):
        print self.display_table()
        print self.first_question()
        
        choice = raw_input("> ")
        self.users_choice(choice)

#creates a dictionary for each year a player was drafted and all players 
#drafted that year        
    def players_by_year(self):
        draft_years_players = {}
    
        for player in self.players:
            draft_year = player.draft_year
            
            if draft_year != '':
                draft_year = int(draft_year)
            else:
                draft_year = 0
                
            if draft_year in draft_years_players:
                draft_years_players[draft_year].append(player)
            else:
                draft_years_players[draft_year] = [player]
        
        return draft_years_players

#creates a table showing each year a player was drafted and how many players
#were drafted that year
    def display_table(self):
        draft_years = []
        draft_years_count = []
        
        for player in self.players:
            draft_year = player.draft_year
            
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
        total_players = sum_table_sorted["No. of Players"].sum()
        players_no_data = sum_table_sorted.loc[0, "No. of Players"]
        sum_table_clean = sum_table_sorted.drop(0, axis=0)
                
        print """\nHere are the number of players still in the league \
from each draft year as of 2017. Note: \
there wasn't draft data for %d of the %d players. It is possible these players \
weren't drafted. \n""" % (players_no_data, total_players)
        
        time.sleep(1)
        return sum_table_clean

#this is the first quesetion asked after displaying the table described in the
#display_table() function
    def first_question(self):
            return """\nAre you curious which players were drafted in a specific year? Of \
course you are! Enter a year, and a list of players drafted that year \
will be provided."""
    
    def users_choice(self, user_choice):
        choice = Choice(user_choice)
        if choice.is_exit_code():
            print "Good bye!"
            sys.exit()
        elif choice.is_NBA_year():
            players = self.players_by_year().get(int(choice.user_choice))
            if players:
                print "\n" + ", ".join(map(lambda p: p.full_name(), players))
            else:
                print "\nNo one drafted in %s was in the NBA as of 2017" % choice
            time.sleep(1)
            self.see_another()
        elif choice.is_year_prior_NBA():
            print "\nThat is prior to the NBA's existance"
            self.see_another()
        elif choice.is_name():
            player = self.find_player_by_name(choice.user_choice)
            if player:
                print player.draft_info()
            else:
                print "\n%s wasn't active in the NBA in 2017." % choice.user_choice.title()
            time.sleep(1)
            self.see_another()
        else:
            print "Try again!"
            time.sleep(1)
            self.see_another()

# allows the user to continue with the applcation            
    def see_another(self):       
        print """\nDo you want to see another year? If so, type that year. Do you \
want to see which year and round a specific player was drafted? If so, \
type that player's name. Feel free to also type 'stop' and you can exit this \
awesome program"""
    
        choice = raw_input('> ')
        
        self.users_choice(choice)
 
# finds the user's player within the player list, if it exists       
    def find_player_by_name(self, user_submitted_name):
        for player in self.players:
            if user_submitted_name.lower() == player.search_name():
                return player
        return None
        
