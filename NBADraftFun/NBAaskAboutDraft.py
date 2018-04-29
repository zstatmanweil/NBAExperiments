import NBANumberofPlayersByDraftYear as nb
import NBAplayerNamesByDraftYear as nbn
import sys
import time

#this script is a way to see if a list of the number of NBA players still 
#active in the NBA by draft year as of 2017 and then get a full list of 
#names for a specific year of interest

#this function will allow the user to continue seeing lists by year 
def see_another():       
    print """\nDo you want to see another year? If so, type that year. Do you \
want to see which year and round a specific player was drafted? If so, \
type that player's name. Feel free to also type 'stop' and you can exit this \
awesome program"""

    choice = raw_input('> ')
    
    users_choice(choice)
    
#this function will allow the user to exit or make a choice
def users_choice(choice):
    if choice == "stop":
        print "Good bye!"
        sys.exit()
    elif choice.isdigit() and len(choice) == 4:
        nbn.get_players_names(choice)
        time.sleep(2)
        see_another()
    elif choice.isdigit() and len(choice) != 4:
        print "\nThat isn't a year"
        time.sleep(1)
        see_another()
    else:
        nbn.get_draft_year_round(choice)
        time.sleep(2)
        see_another()

nb.get_number_players()

print """\nAre you curious which players were drafted in a specific year? Of \
course you are! Enter a year, and a list of players drafted that year \
will be provided."""

time.sleep(1)
choice = raw_input('> ')

users_choice(choice)

time.sleep(1)
see_another()