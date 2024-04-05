from users import User
from ui import MenuUi
from languages import Language


def giris():
    giris_menu = MenuUi(["GİRİŞ YAP",
                         "KAYIT OL",
                         "ÇIKIŞ"])
    giris_menu.show_menu()
    x = giris_menu.get_choise()
    if x == 1:
        username = input("Kullanıcı adınızı giriniz: ")
        password = input("Şifrenizi giriniz: ")
        return User(username, password).giris_yap()
    elif x == 2:
        username = input("Kullanıcı adınızı giriniz: ")
        password = input("Şifrenizi giriniz: ")
        return User(username, password).kayit_ol()
    elif x == 3:
        return False
    else:
        print("Hatalı seçim yaptınız")
        return False


def dil_secimi():
    ana_menu = MenuUi(["INGILIZCE",
                       "ALMANCA",
                       "FRANSIZCA",
                       "çıkış yap",
                       ])
    ana_menu.show_menu()
    y = ana_menu.get_choise()
    if y == 1:
        print("İngilizce seçildi")
        return Language().set_language("İngilizce")
    elif y == 2:
        print("Almanca seçildi")
        return Language().set_language("Almanca")
    elif y == 3:
        print("Fransızca seçildi")
        return Language().set_language("Fransızca")
    elif y == 4:
        print("Çıkış yapılıyor...")
        return False
    else:
        print("Hatalı seçim yaptınız")
        return False


def menu(language_object):
    ana_menu = MenuUi(["KELİMELERİ LİSTELE",
                       "KELİME ÖĞREN",
                       "KLASİK TEST YAP",
                       "ÇOKTAN SEÇMELİ TEST YAP",
                       "DIL SECİMİNE DÖN",
                       "ÇIKIŞ YAP",
                       ])
    ana_menu.show_menu()
    z = ana_menu.get_choise()
    if z == 1:
        print("Kelimeleri listele seçildi")
        language_object.kelime_listele()
    elif z == 2:
        print("Kelime öğren seçildi")
        language_object.kelime_ogren()
    elif z == 3:
        print("Klasik test yap seçildi")
        language_object.klasik_test()
    elif z == 4:
        print("Çoktan seçmeli test yap seçildi")
        language_object.coktan_secimli_test()
    elif z == 5:
        print("Dil seçimine dön seçildi")
        return dil_secimi()
    elif z == 6:
        print("Çıkış yapılıyor...")
        exit()
    else:
        print("Hatalı seçim yaptınız")


if __name__ == "__main__":
    if giris():
        language = dil_secimi()
        if not language:
            print("Çıkış yapılıyor...")
        else:
            while True:
                menu(language)
                if menu(language) is not None:
                    language = menu(language)

    else:
        print("Çıkış yapılıyor...")
