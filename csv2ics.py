#!/usr/bin/python3

import csv
import datetime
from ics import Calendar, Event

c = Calendar()

csv_file = open('ct.csv')
csv_reader = csv.DictReader(csv_file, delimiter=',')

for row in csv_reader:

    e = Event()

    if str(row["note"]) == "":
        e.name = "c't {}".format(row["title"])
    else:
        e.name = "c't {} ({})".format(row["title"], row["note"])

    e.begin = datetime.datetime.strptime(row["date"],'%d.%m.%Y').isoformat()
    e.make_all_day()

    c.events.add(e)

# Print calendar as string to stdout
print(str(c))
