import json

#npaplayers.json found here: http://data.nba.net/10s/prod/v1/2017/players.json
json_file = open('nbaplayers.json')
json_str = json_file.read()
json_data = json.loads(json_str)

players = json_data['league']['standard']

def get_height(player):
    return int(player['heightFeet']) * 12 + int(player['heightInches'])

total_height = 0
player_count = 0
for player in players:
    try:
        height = get_height(player)
        total_height += height
        player_count += 1
    except ValueError:
        pass

avg_height_in = total_height / player_count
avg_height_ft = avg_height_in / 12
avg_height_ft_in = avg_height_in % 12

print """The average height of an NBA \
player in 2017 was %d' %d\" """ % (avg_height_ft, avg_height_ft_in)
