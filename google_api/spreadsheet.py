import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets']
creds = gspread.service_account(filename='./client_secret.json')


sheet = creds.open('yuma_sample').sheet1

data = sheet.get_all_records()

print(data)