# ===================================
# Stock Trend Probability System
# Using Google Sheets Link
# ===================================


import csv
import requests
from io import StringIO

# Google Sheets CSV export link
sheet_url = "https://docs.google.com/spreadsheets/d/your_sheet_id/export?format=csv"

# Download sheet data
response = requests.get(sheet_url)

# Convert CSV text into readable format
csv_data = StringIO(response.text)

# Read CSV data
reader = csv.DictReader(csv_data)

data = []

for row in reader:
    data.append(row)

print("Google Sheet Dataset Loaded Successfully!\n")

print("Available Stocks:\n")

# Showing available stock names
stock_names = []

for row in data:
    stock_names.append(row["Stock"])

for stock in stock_names:
    print("-", stock)

# User input
user_input = input("\nEnter stock name: ")

# Stock probability analysis
stock_scores = {}

for row in data:

    stock = row["Stock"]

    if row["Up_Probability"] == "":
        continue

    up_probability = float(row["Up_Probability"])
    down_probability = float(row["Down_Probability"])

    stock_scores[stock] = {
        "Up": up_probability,
        "Down": down_probability
    }

# Display result
print("\nStock Trend Prediction:\n")

found = False

for stock, values in stock_scores.items():

    if stock.lower() == user_input.lower():

        print(f"Stock: {stock}")
        print(f"Probability of Going Up: {values['Up']}%")
        print(f"Probability of Going Down: {values['Down']}%")

        if values['Up'] > values['Down']:
            print("\nPrediction: Stock is more likely to rise.")
        else:
            print("\nPrediction: Stock is more likely to fall.")

        found = True

# If stock not found
if found == False:
    print("Stock not found in dataset.")
