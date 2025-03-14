import dateparser

date_strings = [
    "31 December 2020",
    "2021-01-02",
    "March 3, 2021",
    "04/04/2022"
]

parsed_dates = [dateparser.parse(x) for x in date_strings]
for date in parsed_dates:
    print(date)