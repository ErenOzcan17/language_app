import csv
import sqlite3

baglanilan_database = sqlite3.connect("database.sqlite")
cursor = baglanilan_database.cursor()

with open('eng-tr_datasest.csv', 'r', newline='') as csv_file:
    files = csv.reader(csv_file)
    for file in files:
        cursor.execute("INSERT INTO english_language (word, meaning) VALUES (?, ?,)", (file[0], file[1]))

baglanilan_database.commit()
baglanilan_database.close()
