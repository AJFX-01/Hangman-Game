
from wordx import wordx
from hangman import get_letter, get_user_letter, level
from unittest.mock import Mock, patch

def main():
    test_getletter()
    test_getuletter()
    test_setts()
    #test_error()


def test_getletter():
    #assert get_letter("testing) == False
    assert get_letter("a") == "a"
    assert get_letter("b") == "b"

def test_getuletter() -> None:
   with patch('builtins.input',new=Mock(return_value='a')):
      assert get_user_letter() == 'a'
   with patch('builtins.input',new=Mock(return_value='c')):
      assert get_user_letter() == 'c'
   #assert get_user_letter() 


def test_level():
    assert level(6, 11) == "High"
    assert level(4, 5) == "Meduim"
    assert level(0, 0) == "Low"
    

   # with pytest.raises(ValueError):
    #    get_user_letter("...")
    
    #with pytest.raises(ValueError):
     #   get_user_letter("1")""""

if __name__ == "__main__":
    main()