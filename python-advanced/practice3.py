# [Medium] - Date Format
# Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.

# Examples

# convert_date("11/12/2019") ➞ "20191211"
 
# convert_date("12/31/2019") ➞ "20193112"
 
# convert_date("01/15/2019") ➞ "20191501"

def convert_date(date):
    date = date.split("/")
    date.reverse()
    date = "".join(date)
    return date

print(convert_date("01/15/2019"))



# date = "11/12/2019"
# date = date.split("/")
# date.reverse()
# date = "".join(date)
# print(date)

# from datetime import datetime
# d1 = datetime.strptime('2020-08-14', '%Y-%m-%d')
# print(d1)

# d2 = datetime(2020, 8, 14, 0, 0)
# d2.strftime('%d %B %Y')
# print(d2)
