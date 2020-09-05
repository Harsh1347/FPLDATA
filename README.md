# FPLDATA :Football:
## Get processed and cleaner data from the FPL API!

## Installation
Run the following code to install:
```python 
pip install fpldata
```

## Usage
### Get the names of team in EPL. Returns a list
```python
from fpldata import get_team_name

teams = get_team_name()
print(teams)
```
### Get the EPL table. Returns a pandas DataFrame

```python
from fpldata import get_table

table = get_table()
print(table)
```
### Compares two teams based on their Strengths scores. Input should be the short name of the team. Returns a pandas DataFrame
```python
from fpldata import team_compare

data = team_compare('ARS','LIV')
print(data)
```

