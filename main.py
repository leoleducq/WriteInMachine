import base64

from utils import dict_char_to_morse


def to_ascii(text : str) -> str:
    try :
        return "".join([str(ord(character)) for character in text])
    except :
        return "Invalid input"
    
def to_base64(text : str) -> str:
    try :
        return base64.b64encode(text.encode("ascii"))
    except :
        return "Invalid input"

def to_hex(text : str) -> str:
    try :
        return text.encode("ascii").hex()
    except :
        return "Invalid input"

def to_binary(text : str) -> str:
    try :
        return " ".join([bin(ord(character))[2:] for character in text])
    except :
        return "Invalid input"

def to_octal(text : str) -> str:
    try :
        return " ".join([oct(ord(character))[2:] for character in text])
    except :
        return "Invalid input"

def to_decimal(text : str) -> str:
    try :
        return " ".join([str(ord(character)) for character in text])
    except :
        return "Invalid input"

def to_morse(english_plain_text : str) -> str:
    try :
        return " ".join([dict_char_to_morse[char.upper()] if char != " " else " " for char in english_plain_text])
    except :
        return "Invalid input"

# Exécute chaque fonction et stocke le résultat dans un fichier texte
def main(text : str) -> str:
    with open("../output.txt", "a", encoding="utf-8") as file :
        file.write(f"Input : {text} \n")
    for function in [to_ascii, to_base64, to_hex, to_binary, to_octal, to_decimal, to_morse]:
        print(f"{function} : {function(text)}")
        with open("../output.txt", "a", encoding="utf-8") as file:
            file.write(f"{function} : {function(text)} \n")

# Tant que l'utilisateur ne quitte pas le programme, on lui demande un texte à convertir
while True :
    text = input("Enter a text to convert : ")
    if text == "quit" :
        break
    main(text)