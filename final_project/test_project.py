import pytest
from project import (
    check_language,
    chosen_lang,
)
from lang_engine import (
    exit_program,
        
)

def test():
    test_exit()
    test_check_language()
    test_chosen_lang()



def test_exit():    
    with pytest.raises(SystemExit) as exitprogram:
        exit_program()
    assert exitprogram.type == SystemExit    
    assert exitprogram.value.code == 0

def test_check_language():
    assert check_language("polski") == 'Jakiego języka chcesz się uczyć? angielski lub niemiecki?: '
    assert check_language("english") == 'Which language would you like to learn? polish or german?: '
    assert check_language("deutsch") == 'Welches Sprache möchtest du lernen? polnisch oder englisch?: '
    assert check_language(" ") == 'Try again, press any key...'
    
def test_chosen_lang():
    assert chosen_lang('angielski') == ('final_project/test.csv', ['angielski', 'angielski'])
    