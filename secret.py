# Chaine de caractère permettant d'encoder/décoder :
code_ = "p+çS#2z8GceHw`Ormè M;%@3g€KRa!^iv1sA,Q9qCIb:NYDhy'/u0oF?éXEkB*jP¨àTxd-_£$(5JWtZl.ùLn=6f4U§&V)7"


def encode(string):
    """
    Fonction d'encadage
    Args :
    string (str): chaine de caractères à encoder
    Return:
    str

    ex : encode("Hello, world !") -> 'wH..FQM`Fm.-M^'
    """
    pass


def decode(string):
    """
    Fonction d'encadage
    Args :
    string (str): chaine de caractères à décoder
    Return :
    str

    ex : decode("wH..FQM`Fm.-M^") -> 'Hello, world !'
    """
    pass


if __name__ == "__main__":
    text = input("Entrez un texte : ")
    print("Encodage : ")
    print(encode(text))

# coucou toi
