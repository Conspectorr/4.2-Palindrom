def palindrom(word):
    """ 
        Sprawdza, czy wyraz jest palindromem.
        Argument:
        word
    """
    reverse_word=word[::-1]
    if word == reverse_word:
        print("Wyraz jest palindromem.")
    else:
        print("Wyraz nie jest palindromem.")
    

palindrom(word)

