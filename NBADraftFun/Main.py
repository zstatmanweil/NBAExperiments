import json
from Application import Application

#npaplayers.json found here: http://data.nba.net/10s/prod/v1/2017/players.json
json_file = open (r'..\nbaplayers.json')
json_str = json_file.read()
json_data = json.loads(json_str)

#accessing each player's dictionary and name
players = json_data['league']['standard']

#instantiating application
app = Application(players)
app.run()

