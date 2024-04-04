import sqlite3

baglanilan_database = sqlite3.connect("database.sqlite")
cursor = baglanilan_database.cursor()


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def kayit_ol(self):
        try:

            cursor.execute("SELECT * FROM users WHERE username = ?", (self.username,))
            if cursor.fetchone():
                print("Bu kullanıcı adı kullanılmaktadır lütfen başka bir kullanıcı adı seçiniz")
            else:
                cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (self.username, self.password))
                baglanilan_database.commit()
                print("Kayıt başarılı")
                return True
        except Exception as e:
            print("Hata oluştu: ", e)
        return False

    def giris_yap(self):
        try:
            cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (self.username, self.password))
            if cursor.fetchone():
                print("Giriş başarılı")
                return True
            else:
                print("Kullanıcı adı veya şifre hatalı")
        except Exception as e:
            print("Hata oluştu: ", e)
        return False
