import pytest
import pandas
from pandas.testing import assert_frame_equal
from fpldata.team_data import TeamData

@pytest.mark.parametrize('test_input,expected', [('ARS', 1), ('CHE', 5),
    ('', {'ARS': 1, 'AVL': 2, 'BHA': 3, 'BUR': 4, 'CHE': 5, 'CRY': 6, 'EVE': 7, 'FUL': 8, 'LEI': 9, 'LEE': 10, 'LIV': 11, 'MCI': 12, 'MUN': 13, 'NEW': 14, 'SHU': 15, 'SOU': 16, 'TOT': 17, 'WBA': 18, 'WHU': 19, 'WOL': 20})])
def test_get_team_id(test_input, expected):
    team_data = TeamData()
    team_id = team_data.get_team_id(test_input)
    assert team_id == expected


def test_list_team_name():
    team_name = TeamData().list_team_name()
    assert team_name  == {'ARS': 'Arsenal', 'AVL': 'Aston Villa', 'BHA': 'Brighton', 'BUR': 'Burnley', 'CHE': 'Chelsea', 'CRY': 'Crystal Palace', 'EVE': 'Everton', 'FUL': 'Fulham', 'LEI': 'Leicester', 'LEE': 'Leeds', 'LIV': 'Liverpool', 'MCI': 'Man City', 'MUN': 'Man Utd', 'NEW': 'Newcastle', 'SHU': 'Sheffield Utd', 'SOU': 'Southampton', 'TOT': 'Spurs', 'WBA': 'West Brom', 'WHU': 'West Ham', 'WOL': 'Wolves'}
