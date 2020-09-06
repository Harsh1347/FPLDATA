from .team_data import TeamData
from .players import PlayerData

# import requests
# import pandas

# def get_team_name():
#     URL = f"https://fantasy.premierleague.com/api/bootstrap-static/"
#     resp = requests.get(URL).json()
#     teams = resp['teams']
#     team_name = []
#     for team in teams:
#         team_name.append(team['name'])
#     return team_name

# def get_table():
#     URL = f"https://fantasy.premierleague.com/api/bootstrap-static/"
#     resp = requests.get(URL).json()
#     teams = resp['teams']
#     table = {'Position':[],'Team':[],'Games Played':[],'Win':[],'Draw':[],'Loss':[],'Points':[],'Form':[]}
#     for team in teams:
#         table['Position'].append(team['position'])
#         table['Team'].append(team['name'])
#         table['Games Played'].append(team['played'])
#         table['Win'].append(team['win'])
#         table['Draw'].append(team['draw'])
#         table['Loss'].append(team['loss'])
#         table['Points'].append(team['points'])
#         table['Form'].append(team['form'])
#     data = pandas.DataFrame(data=table)
#     return data

# def team_compare(team1,team2):
#     URL = f"https://fantasy.premierleague.com/api/bootstrap-static/"
#     resp = requests.get(URL).json()
#     teams = resp['teams']
#     stats = {'Team':[],'Strength':[],'Overall Home Strength':[],'Overall Away Strength':[],
#             'Home Attack':[],'Away Attack':[],'Home Defence':[],'Away Defence':[] }
#     team_list = [team1,team2]
#     for team in team_list:
#         for t in teams:
#             if t['short_name'].lower() == team.lower():
#                 stats['Team'].append(t['name'])
#                 stats['Strength'].append(t['strength'] )
#                 stats['Overall Home Strength'].append(t['strength_overall_home'])
#                 stats['Overall Away Strength'].append(t['strength_overall_away'])
#                 stats['Home Attack'].append(t['strength_attack_home'])
#                 stats['Away Attack'].append(t['strength_attack_away'])
#                 stats['Home Defence'].append(t['strength_defence_home'])
#                 stats['Away Defence'].append(t['strength_defence_away'])
#     data = pandas.DataFrame(data=stats)
#     return data
