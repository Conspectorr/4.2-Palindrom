from operator import length_hint


def palindrom(word):
    """ 
        Sprawdza, czy wyraz jest palindromem.
        Argument:
        word
    """
    if len(word) % 2 ==0:
        print("Wyraz nie jest palindromem.")
    else:
        print("Wyraz ma nieparzystą ilość liter.")


