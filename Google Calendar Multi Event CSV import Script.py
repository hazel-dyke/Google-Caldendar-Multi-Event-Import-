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

#   Create a file called "last_sats_and_paydays.csv".
with open('last_sats_and_paydays.csv', 'w') as f:
    print("file created")

#   Write a heading to the file that will make it suitable for a Google calendar import, which expects the following columns:
#   Subject, Start Date, All Day Event, Start Time, End Time, Location, Description (Only the first 2 headers in this list are required. The rest are optional.)

with open('last_sats_and_paydays.csv', 'r+') as f:
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
        months = range(1, 13)
        #   paydays (last working days before the 29th of each month):
        for month in months:
            last_days = (calendar.monthcalendar(year, month)[-1:][0][:5])
            if 28 in last_days:
                date_string = f"{list(calendar.month_abbr).index(calendar.month_abbr[month]):02d}" +"/"+ "28" +"/"+  f"{year}"
                print(date_string)
                f.write("Payday" + "," + date_string + "," + "TRUE" + '\n')
            elif 27 in last_days:
                date_string = f"{list(calendar.month_abbr).index(calendar.month_abbr[month]):02d}" +"/"+ "27" +"/"+  f"{year}"
                print(date_string)
                f.write("Payday" + "," + date_string + "," + "TRUE" + '\n')
            elif 26 in last_days:
                date_string = f"{list(calendar.month_abbr).index(calendar.month_abbr[month]):02d}" +"/"+ "26" +"/"+  f"{year}"
                print(date_string)
                f.write("Payday" + "," + date_string + "," + "TRUE" + '\n')
            elif 29 == last_days[0]:
                date_string = f"{list(calendar.month_abbr).index(calendar.month_abbr[month]):02d}" +"/"+ "26" +"/"+ f"{year}"
                print(date_string)
                f.write("Payday" + "," + date_string + "," + "TRUE" +'\n')
            elif 30 == last_days[0]:
                date_string = f"{list(calendar.month_abbr).index(calendar.month_abbr[month]):02d}" +"/"+ "27" +"/"+ f"{year}"
                print(date_string)
                f.write("Payday" + "," + date_string + "," + "TRUE" + '\n')
            elif 31 == last_days[0]:
                date_string = f"{list(calendar.month_abbr).index(calendar.month_abbr[month]):02d}" +"/"+ "28" +"/"+ f"{year}"
                print(date_string)
                f.write("Payday" + "," + date_string + "," + "TRUE" + '\n')

