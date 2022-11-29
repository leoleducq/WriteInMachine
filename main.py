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
    with open(f"output.txt", "a", encoding="utf-8") as file :
        print(file.write(f"Input : {text} \n"))
        print(file.write(f"ASCII : {to_ascii(text)} \n"))
        print(file.write(f"Base64 : {to_base64(text)} \n"))
        print(file.write(f"Hex : {to_hex(text)} \n"))
        print(file.write(f"Binary : {to_binary(text)} \n"))
        print(file.write(f"Octal : {to_octal(text)} \n"))
        print(file.write(f"Decimal : {to_decimal(text)} \n"))
        print(file.write(f"Morse : {to_morse(text)} \n"))

main(input("Enter a string : "))