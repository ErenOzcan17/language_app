import sqlite3
from ui import QuestionUi

baglanilan_database = sqlite3.connect("database.sqlite")
cursor = baglanilan_database.cursor()


class Language:
    def __init__(self):
        self.LANGUAGES_DICT = {"İngilizce": "english_language", "Almanca": "german_language",
                               "Rusça": "russian_language"}
        self.LANGUAGE = ""
        self.TABLE_NAME = ""

    def set_language(self, dil):
        self.LANGUAGE = dil
        if dil in self.LANGUAGES_DICT:
            self.TABLE_NAME = self.LANGUAGES_DICT[dil]
            return self
        else:
            print("Dil desteklenmiyor.")

    def kelime_listele(self):
        cursor.execute(f"SELECT * FROM {self.TABLE_NAME}")
        for kelime in cursor.fetchall():
            print(kelime)

    def kelime_ogren(self):
        cursor.execute(f"SELECT word, meaning FROM {self.TABLE_NAME} ORDER BY RANDOM() LIMIT 1")
        row = cursor.fetchone()
        print(row)

    def klasik_test(self):
        while True:
            cursor.execute(f"SELECT * FROM {self.TABLE_NAME} ORDER BY RANDOM() LIMIT 1")
            row = cursor.fetchone()
            print(row[1])
            cevap = input("Kelimenin anlamını giriniz: ")
            if cevap.lower() == row[2].lower():
                print("Doğru bildiniz")
            else:
                print("Yanlış cevap")
            devam = input("Devam etmek istiyor musunuz? [e/h]")
            if devam.lower() == "h":
                break

    def coktan_secimli_test(self):
        while True:
            try:
                cursor.execute(f"SELECT * FROM {self.TABLE_NAME} ORDER BY RANDOM() LIMIT 1")
                question = cursor.fetchone()
                cursor.execute(f"SELECT * FROM {self.TABLE_NAME} ORDER BY RANDOM() LIMIT 4")
                choise = cursor.fetchall()
                question_object = QuestionUi(question, choise)
                question_object.show_question()
                answer = int(input("Lütfen cevabınızı giriniz [1-4]: "))
                assert 1 <= answer <= 4, "Lütfen [1-4] aralığında bir değer giriniz"
                if answer == 4:
                    print("Doğru bildiniz")
                else:
                    print("Yanlış cevap")
                devam = input("Devam etmek istiyor musunuz? [e/h]")
                if devam.lower() == "h":
                    break
            except Exception as e:
                print(e)

