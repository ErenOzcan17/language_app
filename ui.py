import random


class MenuUi:
    def __init__(self, menu_items):
        self.Menu_items = menu_items

    def show_menu(self):
        print("-" * 50, "|{:*^50}|".format("MENÜ"), "-" * 50, sep="\n")
        for no, item in enumerate(self.Menu_items):
            print("|{:^50}|".format(str(no + 1) + "..." + item))
        print("-" * 52)

    def get_choise(self):
        while True:
            try:
                choise = int(input(f"lütfen tercihinizi giriniz [1-{len(self.Menu_items)}]: "))
                assert 1 <= choise <= len(self.Menu_items), (f"lütfen [1-{len(self.Menu_items)}]"
                                                             f": aralığında bir değer giriniz: ")
                return choise
            except Exception as e:
                print(e)
            if not Exception:
                break


class QuestionUi:
    def __init__(self, question, choices):
        self.question = question
        self.choices = choices

    def show_question(self):
        random.shuffle(self.choices)
        print("-" * 100, "|{:*^99}|".format("SORU"), "-" * 100, sep="\n")
        print("|{:^99}|".format(self.question[1]), "-" * 100, sep="\n")
        x = 1
        for choice in self.choices:
            print("|{:^99}|".format(str(x) + "..." + choice[2]))
            if choice == self.question:
                correct_answer = x
            x += 1
        print("-" * 100)

        return correct_answer



