import datetime

# print today
today = datetime.datetime.now()
# today
datetime.datetime(2023, 8, 4, 18, 14, 5, 604539)
type(today)
# <class 'datetime.datetime'>
someday = datetime.datetime(2023, 8, 3)

someday -today
# datetime.timedelta(days=-5, seconds=50505, microseconds=940281)
datetime.datetime(2012,2,2)
# datetime.datetime(2012, 2, 2, 0, 0)
50578 /(24*60*60)
# 0.5853935185185185
somedelta = someday -today
type(somedelta)
# <class 'datetime.timedelta'>

somedelta.days
# -5
pass