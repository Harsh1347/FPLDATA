import requests
import pandas
class TeamData:
    URL = f"https://fantasy.premierleague.com/api/bootstrap-static/"
    resp = requests.get(URL).json()
    teams = resp['teams']
    # events = resp['events']
    # elements = resp['elements']
    
    def __init__(self):    
        self.team_name = {}
        self.team_id = {}
        for team in self.teams:
            self.team_name[team['short_name']] = team['name']
            self.team_id[team['short_name']] = team['id']

    def team_compare(self,team1,team2):
        self.stats = {'Team':[],'Strength':[],'Overall Home Strength':[],'Overall Away Strength':[],
                'Home Attack':[],'Away Attack':[],'Home Defence':[],'Away Defence':[] }
        self.team_list = [team1,team2]
        for team in self.team_list:
            for t in self.teams:
                if t['short_name'].lower() == team.lower():
                    self.stats['Team'].append(t['short_name'])
                    self.stats['Strength'].append(t['strength'] )
                    self.stats['Overall Home Strength'].append(t['strength_overall_home'])
                    self.stats['Overall Away Strength'].append(t['strength_overall_away'])
                    self.stats['Home Attack'].append(t['strength_attack_home'])
                    self.stats['Away Attack'].append(t['strength_attack_away'])
                    self.stats['Home Defence'].append(t['strength_defence_home'])
                    self.stats['Away Defence'].append(t['strength_defence_away'])
        self.data = pandas.DataFrame(data=self.stats,index=self.stats['Team'])
        del(self.data['Team'])
        return self.data
    
    def list_team_name(self):
        return self.team_name

    def get_team_id(self,team1 = ""):
        if team1:
            return self.team_id[team1.upper()]
        else:
            return self.team_id
