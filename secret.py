# Chaine de caractère permettant d'encoder/décoder :
code_ = "p+çS#2z8GceHw`Ormè M;%@3g€KRa!^iv1sA,Q9qCIb:NYDhy'/u0oF?éXEkB*jP¨àTxd-_£$(5JWtZl.ùLn=6f4U§&V)7"
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

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


def decode(string,clef):
    """
    Fonction d'encadage
    Args :
    string (str): chaine de caractères à décoder
    Return :
    str

    ex : decode("wH..FQM`Fm.-M^") -> 'Hello, world !'
    """
    for caractere in code_:
        phrase_decryptee = ""  # Initialisation de la phrase déchiffrée
        if caractere.isalpha():  # Vérifie si le caractère est une lettre avec la méthode isalpha()
            indice = (alphabet.index(caractere) - clef) % len(alphabet)  # Calcule le nouvel indice déchiffré
            phrase_decryptee += alphabet[indice]  # Ajoute la lettre déchiffrée à la phrase
        else:
            phrase_decryptee += caractere  # Si le caractère n'est pas une lettre, ajoute-le tel quel
    return phrase_decryptee  # Retourne la phrase déchiffrée
    


if __name__ == "__main__":
    text = input("Entrez un texte : ")
    print("Encodage : ")
    print(encode(text))
