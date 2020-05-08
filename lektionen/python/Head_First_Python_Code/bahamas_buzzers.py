import pprint
from datetime import datetime

def convert2ampm(time24: str) -> str:
  """Converts a 24h-format time-string into am-pm-format time-string."""
  return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


with open('buzzers.csv') as data:
  ignore = data.readline()
  flights = {}
  for line in data:
    k, v = line.strip().split(',')
    flights[k] = v
  # flights = {k: v.strip().split(',') for k, v in data}  

pprint.pprint(flights)
print()

# flights2 = {}
# for k, v in flights.items():
#   flights2[convert2ampm(k)] = v.title()

# pprint.pprint(flights2)
more_flights = {convert2ampm(k): v.title() for k, v in flights.items()}

pprint.pprint(more_flights)
print()


just_freeport = {convert2ampm(k): v.title() for k, v in flights.items() if v=='FREEPORT'}
pprint.pprint(just_freeport)