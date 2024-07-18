
    # Learn_Top_Words
    #### Video Demo:  <URL HERE>
    #### Description:
    
        A program for learning the most frequently used words in a selected language. (Polish, English, German).

        The program allows you to choose one of three main languages ​​in which communication will take place: Polish, English, German.

        After selecting the guide language, the user can choose one of two languages ​​to learn:
        1. For Polish, learning English, German
        2. For English, learning Polish, German
        3. For German, learning English, Polish
        
        After selecting the language to learn, the program starts printing words to translate.
        If the answer is correct, a printout with the current score will appear, e.g.; "Your actual score 45 out of 100 points"
        If the answer is false, the correct translation of the word will be printed and the program will continue entering another word.
        Once all words have been answered correctly, a message with the actual score (maximum score) will be displayed and the printout will indicate that all words have been translated and the program will close.

        Program includes:
        project.py - main program.
        lang_engine.py - code for printing words, printing actual score, etc - engine of essential program
        test_project.py - testing cases.
        level1.csv - list 100 top words in three languages to study.
        test.csv - list 3 words for testing.