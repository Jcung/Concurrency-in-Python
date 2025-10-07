from datetime import date, datetime

# 13.1 — Write today's date to a file
today = date.today()
with open('today.txt', 'w') as file:
    file.write(str(today))

# 13.2 — Read the text file into a string
with open('today.txt', 'r') as file:
    today_string = file.read()

print("String read from file:", today_string)

# 13.3 — Parse the date from the string
parsed_date = datetime.strptime(today_string, '%Y-%m-%d').date()
print("Parsed date:", parsed_date)
