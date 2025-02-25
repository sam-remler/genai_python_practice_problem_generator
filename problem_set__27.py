"""```python
# Title: Day of the Month, Thanksgiving

# Difficulty: Medium

"""

import calendar

def thanksgiving_day(year : int):
    cal = calendar.Calendar()
    days = [day[0] for day in cal.itermonthdays2(year, 11) if day[0] > 0 and day[1] == 3]
    
    return days[3]

print( thanksgiving_day (2023) )