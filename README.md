# FPLDATA
Get processed and cleaner data from the FPL API!

## Installation
Run the following code to install:
```python 
pip install fpldata
```

## Usage
```python
from fpldata import get_team_name

# Get the names of team in EPL. Returns a list
teams = get_team_name()
print(teams)

from fpldata import get_table()

# Get the EPL table. Returns a pandas DataFrame
table = get_table()
print(table)

from fpldata import team_compare

# Compares two teams based on their Strengths scores. Input should be the short name of the team. Returns a pandas DataFrame
data = team_compare('ARS','LIV')
print(data)
```

