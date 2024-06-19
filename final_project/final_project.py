"""Importing"""
import random
import sys
from lang import exit_program, pol_lang, eng_lang, de_lang

language_list = ["angielski", "niemiecki", "polish", "german", "polnisch", "englisch"]
word_list: list = []
typed_lang_study: list = []
def main():
    """Main program"""
    while True:
        language = input("Choose your language: polski, english or deutsch: ").lower()
        learn_lang = input(check_language(language)).lower()
        try:
            with open(chosen_lang(learn_lang)[0], "r", encoding="utf-8") as file_level:
                for line in file_level:
                    line = line.lower()
                    pl, eng, de = line.strip().split(",")
                    word_list.append({"pl":pl, "eng":eng, "de":de})
        except (NameError, TypeError):
            print("You need to select the program language: polski, english or deutsch\n"
                  "Musisz wybrać język programu: polski, english lub deutsch\n"
                  "Sie müssen die Programmsprache auswählen: polski, english oder deutsch")
            continue
        else:
            break
    lang_selection(language)

def check_language(language):
    """check chosen language and run proper"""
    translate = {
                 "pl":"Jakiego języka chcesz się uczyć? angielski lub niemiecki?: ",
                 "eng":"Which language would you like to learn? polish or german?: ",
                 "de":"Welches Sprache möchtest du lernen? polnisch oder englisch?: "
                 }
    if language == "polski":
        return translate["pl"]
    if language == "english":
        return translate["eng"]
    if language == "deutsch":
        return translate["de"]
    if language == "exit program":
        exit_program()
    return None
def chosen_lang(learn_lang):
    """Checking and choosing proper file with words and translations"""
    if learn_lang in language_list:
        typed_lang_study.append(learn_lang)
        file_level = "level1.csv"
        return file_level, typed_lang_study
    if learn_lang == "exit program":
        exit_program()
    return None

def lang_selection(language):
    """Chosing proper program function depends of chosen program language and runs the target program(function)"""
    if language == "polski":
        return pol_lang()
    if language == "english":
        return eng_lang()
    if language == "deutsch":
        return de_lang()
    return None

if __name__ == "__main__":
    main()