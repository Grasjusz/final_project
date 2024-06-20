import sys



language_list = ["angielski", "niemiecki", "polish", "german", "polnisch", "englisch"]

def exit_program():
    """Exit program function"""
    print("Exiting the program...")
    sys.exit(0)

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