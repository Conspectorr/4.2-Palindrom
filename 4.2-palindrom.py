def palindrom(word):
    """ 
        Sprawdza, czy wyraz jest palindromem.
        Argument:
        word
    """
    word=word.lower()
    reverse_word=word[::-1]
    if word == reverse_word:
        print("Wyraz jest palindromem.")
    else:
        print("Wyraz nie jest palindromem.")


word= input("Podaj wyraz do sprawdzenia:")
palindrom(word)