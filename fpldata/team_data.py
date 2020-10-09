import requests
import pandas


class TeamData:
    """
    Module for getting data related to team.
    """

    def __init__(self):
        URL = f"https://fantasy.premierleague.com/api/bootstrap-static/"
        resp = requests.get(URL).json()
        self.teams = resp['teams']
        self.events = resp['events']
        self.elements = resp['elements']
        self.team_name = {}
        self.team_id = {}
        for team in self.teams:
            self.team_name[team['short_name']] = team['name']
            self.team_id[team['short_name']] = team['id']

    def team_compare(self, team1, team2):
        """
        Returns a pandas dataframe comparing two teams based on their abilities.

        :param team1: Short name of the first team.
        :type team1: string

        :param team2: Short name of the second team.
        :type team2: string
        """

        self.stats = {
            'Team': [],
            'Strength': [],
            'Overall Home Strength': [],
            'Overall Away Strength': [],
            'Home Attack': [],
            'Away Attack': [],
            'Home Defence': [],
            'Away Defence': []}
        self.team_list = [team1, team2]
        for team in self.team_list:
            for t in self.teams:
                if t['short_name'].lower() == team.lower():
                    self.stats['Team'].append(t['short_name'])
                    self.stats['Strength'].append(t['strength'])
                    self.stats['Overall Home Strength'].append(
                        t['strength_overall_home'])
                    self.stats['Overall Away Strength'].append(
                        t['strength_overall_away'])
                    self.stats['Home Attack'].append(t['strength_attack_home'])
                    self.stats['Away Attack'].append(t['strength_attack_away'])
                    self.stats['Home Defence'].append(
                        t['strength_defence_home'])
                    self.stats['Away Defence'].append(
                        t['strength_defence_away'])
        self.data = pandas.DataFrame(data=self.stats, index=self.stats['Team'])
        del(self.data['Team'])
        return self.data

    def list_team_name(self):
        """
        Returns a dictionary with team id as key and Short Team Name as value.
        """
        return self.team_name

    def get_team_id(self, team1=""):
        """
        Returns the team id if team1 parameter is provided else a dictionary is returned with all the team id and corresponding short name.

        :param team1: Short name of the first team.
        :type team1: string

        """
        try:
            return self.team_id[team1.upper()] if team1 else self.team_id
        except KeyError as err:
            print('Error!', err)
            raise

    def get_table(self):
        """
        Returns EPL table as a pandas dataframe
        """
        self.table = {
            'Position': [],
            'Team': [],
            'Games Played': [],
            'Win': [],
            'Draw': [],
            'Loss': [],
            'Points': [],
            'Form': []}
        for team in self.teams:
            self.table['Position'].append(team['position'])
            self.table['Team'].append(team['name'])
            self.table['Games Played'].append(team['played'])
            self.table['Win'].append(team['win'])
            self.table['Draw'].append(team['draw'])
            self.table['Loss'].append(team['loss'])
            self.table['Points'].append(team['points'])
            self.table['Form'].append(team['form'])
        self.table = pandas.DataFrame(
            data=self.table, index=self.table['Position'])

        del(self.table['Position'])
        return self.table
