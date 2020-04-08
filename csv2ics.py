#!/usr/bin/python3

import csv
import datetime
import uuid
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

    # Generates deterministic uids from a random (fixed) base UUID and the (unique) event names, using SHA1
    base_namespace = uuid.UUID('fc222562-67a1-44e4-9080-64e22818c944')
    e.uid = str(uuid.uuid5(base_namespace, row["title"]))

    e.begin = datetime.datetime.strptime(row["date"],'%d.%m.%Y').isoformat()
    e.make_all_day()

    c.events.add(e)

# Print calendar as string to stdout
print(str(c))
