import csv
import sqlite3

baglanilan_database = sqlite3.connect("database.sqlite")
cursor = baglanilan_database.cursor()

with open('en-fr.csv', 'r', newline='') as csv_file:
    print("CSV dosyası okunuyor...")
    file = csv.reader(csv_file)
    for index, satir in enumerate(file, start=1):
        print(f'{index}. satır ekleniyor')
        cursor.execute("INSERT INTO french_language (word, meaning) VALUES (?, ?)", (satir[0], satir[1]))

baglanilan_database.commit()
baglanilan_database.close()
