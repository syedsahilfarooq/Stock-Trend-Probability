# ===================================
# Disease Prediction System
# Using Google Sheets Link
# =================================== 


import csv
import requests
from io import StringIO

# Google Sheets CSV export link
sheet_url = "https://docs.google.com/spreadsheets/d/1aDGwcTLHmwvrPnSYHSoDz2YvjzK5qGB6QE8tYY9IKEI/export?format=csv"

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

# Available symptoms
symptoms = list(data[0].keys())[1:-1]

print("Common Cold , Influenza , COVID-19 ,Malaria ,Dengue , Typhoid , Pneumonia , Tuberculosis , Migraine , Sinusitis , Bronchitis , Asthma , Chickenpox , Meningitis , Gastroenteritis , Hepatitis A , Measles , Allergic Rhinitis , Ear Infection , Urinary Tract Infection , Food Poisoning , Strep Throat , RSV Infection , Whooping Cough, Lyme Disease:\n")

for symptom in symptoms:
    print("-", symptom)

# User input
user_input = input("\nEnter symptoms separated by commas such as Fever , Cough , Headache: ")

user_symptoms = [s.strip() for s in user_input.split(",")]

# Disease prediction
disease_scores = {}

for row in data:

    disease = row["Disease"]

    if row["Prior"] == "":
        continue
        
    score = float(row["Prior"])

    for symptom in user_symptoms:

        if symptom in symptoms:
            score *= float(row[symptom])

    disease_scores[disease] = score

# Normalize probabilities
total = sum(disease_scores.values())

print("\nPrediction Results:\n")

for disease, score in disease_scores.items():

    probability = (score / total) * 100

    print(f"{disease}: {probability:.2f}%")

# Most likely disease
most_likely = max(disease_scores, key=disease_scores.get)

print("\nMost Likely Disease:", most_likely)
