import gspread


creds = gspread.service_account(filename='./client_secret.json')


sheet = creds.open('yuma_sample').sheet1 # the .json and google sheet are a personal sample.

data = sheet.get_all_records()

print(data)