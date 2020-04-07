# _c't – magazin für computertechnik_ release dates

This repository contains the release dates for coming c't magazines in both [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) and [iCalendar](https://en.wikipedia.org/wiki/ICalendar) formats.

This repository will be kept up-to-date in the future, as soon as new release dates are announced by Heise Medien GmbH.

## Sources for `ct.csv`

 * [2020](https://www.heise.de/mediadaten/downloads/88/1/0/1/5/3/3/2/ct_Mediadaten_2020_Ansicht_neu.pdf)

## Generating the `ics` file from CSV

The included python script generates an `ics` file out of a `csv` file, for usage in a calendar software of your choice.

```shell
user@host:~ $ ./csv2ics.py >> feed.ics
```
