#   Python script to get the last Saturday of the month for the next year and also the last working day (Mon - Fri) before the 29th of each month.
#   Script prints dates to the console and also generates a csv file that is compatible for an import into Google Calendar.
#   Guide for doing the Google calendar import can be found here:
#   https://support.google.com/calendar/answer/37118?hl=en&co=GENIE.Platform%3DDesktop


import sys
import calendar
import time
import datetime

start_year = 2020
end_year = 2020

"""Functions"""
def is_weekday(date):
    return date.weekday() < 5

# A function to get the last working day before the 29th of each month of the year
def get_last_day_of_month(year):
    for month in range(1,13):
        for day in range(28, 0, -1):
            date = datetime.date(year, month, day)
            if is_weekday(date) and day <= 28:
                date_string = f"{month:02d}" + "/" + str(day) + "/" + f"{year}"
                print(date_string)
                f.write("Payday" + "," + date_string + "," + "TRUE" + '\n')
                break
        else:
            continue
    return
"""end of Functions"""

#   Create a file called "last_sats_and_paydays.csv".
with open('last_sats_and_paydays_v2.csv', 'w') as f:
    print("file created")

#   Write a heading to the file that will make it suitable for a Google calendar import, which expects the following columns:
#   Subject, Start Date, All Day Event, Start Time, End Time, Location, Description (Only the first 2 headers in this list are required. The rest are optional.)

with open('last_sats_and_paydays_v2.csv', 'r+') as f:
    f.write("Subject" + "," + "start date" + "," + "All Day Event" + '\n')


# Loop through years and months and write the last saturday paydays to the csv file.
# Dates must be in the format MM/DD/YYYY so that it is compatible with a Google calendar csv import.
    for year in list(range(start_year, end_year+1)):
        print("\n")
        print(f"Last Saturday of each month in {year}")

        if len(sys.argv) > 1:
            try:
                year = int(sys.argv[-1])
            except ValueError:
                pass
            f.write("subject" + "," + "Date" + "," + "TRUE" + "\n")

        #   last Saturdays:
        for month in range(1, 13):
            last_saturday = max(week[-1] for week in calendar.monthcalendar(year, month)) - 1
            # Note that the date string relies on a dictionary to get the appropriate form for Google calendar
            # Number - to - Abbr :  calendar.month_abbr[month_number_var]
            # Abbr - to - Number : list(calendar.month_abbr).index(month_abbr_var)
            date_string = '{:02d}/{}/{}'.format(list(calendar.month_abbr).index(calendar.month_abbr[month]), last_saturday, year)
            print(date_string)
            f.write("Last Saturday" + "," + date_string + "," + "TRUE" + '\n')


        print("\n")
        print(f"{year} paydays (last working day before the 29th!)")

        for year in range (start_year, end_year+1):
            get_last_day_of_month(year)
