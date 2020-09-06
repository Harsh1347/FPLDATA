# FPLDATA :soccer:
## Get processed and cleaner data from the FPL API!

## Installation
Run the following code to install:
```python 
pip install fpldata
```

## Usage
### Get the names of team in EPL. Returns a list
```python
from fpldata import TeamData

t1 = TeamData()
print(t1.get_team_name())
```
### Get the EPL table. Returns a pandas DataFrame

```python
from fpldata import TeamData
t1 = TeamData()
print(t1.get_table())
```
### Compares two teams based on their Strengths scores. Input should be the short name of the team. Returns a pandas DataFrame
```python
from fpldata import TeamData
t1 = TeamData()
data = t1.team_compare('ARS','LIV')
print(data)
```

### Get player list with their id. Returns dictionary of players with ids as key and name as value
```python
from fpldata import PlayerData
p1 = PlayerData()
print(p1.player_list())
```

### Search player by name. Returns dictionary of player with ids as key and name as value
```python
from fpldata import TeamData
t1 = TeamData()
data = t1.search_player('David')
print(data)
```

