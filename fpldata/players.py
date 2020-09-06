import requests
import pandas
class PlayerData:
    URL = f"https://fantasy.premierleague.com/api/bootstrap-static/"
    resp = requests.get(URL).json()
    teams = resp['teams']
    events = resp['events']
    elements = resp['elements']
    info = ['chance_of_playing_next_round', 'chance_of_playing_this_round', 'code', 'cost_change_event',
    'cost_change_event_fall', 'cost_change_start', 'cost_change_start_fall', 'dreamteam_count',
    'element_type', 'ep_next', 'ep_this', 'event_points', 'first_name', 'form', 'id', 'in_dreamteam',
    'news', 'news_added', 'now_cost', 'photo', 'points_per_game', 'second_name', 'selected_by_percent', 
    'special', 'squad_number', 'status', 'team', 'team_code', 'total_points', 'transfers_in', 
    'transfers_in_event', 'transfers_out', 'transfers_out_event', 'value_form', 'value_season','web_name', 
    'minutes', 'goals_scored', 'assists', 'clean_sheets', 'goals_conceded', 'own_goals', 'penalties_saved',
    'penalties_missed', 'yellow_cards', 'red_cards', 'saves', 'bonus', 'bps', 'influence', 'creativity', 
    'threat', 'ict_index', 'influence_rank', 'influence_rank_type', 'creativity_rank', 'creativity_rank_type',
    'threat_rank', 'threat_rank_type', 'ict_index_rank', 'ict_index_rank_type']

    def __init__(self):    
        self.player_info = {k : [] for k in self.info}
        for player in self.elements:
            for v in self.player_info:
                self.player_info[v].append(player[v])
        
    
    def all_player_info(self):
        self.data = pandas.DataFrame(self.player_info)
        self.data['element_type'] = self.data['element_type'].replace([1,2,3,4],['GKP','DEF','MID','FWD'])
        
        return self.data

    def search_player(self,player_name):
        self.op = {}
        for player in self.elements:
            if player_name.lower() in player['first_name'].lower() or  player_name.lower() in player['second_name'].lower():
                self.op[player['id']] = player['first_name']+" "+player['second_name']
        return self.op

    def player_list(self):
        self.players = {}
        for player in self.elements:
            self.players[player['id']] = player['first_name']+" "+player['second_name']
        return self.players