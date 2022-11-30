import base64

from utils import dict_char_to_morse

class Machina :
    def __init__(self, text):
        self.main(text)

    def to_ascii(self, text : str) -> str:
        try :
            return "".join([str(ord(character)) for character in text])
        except :
            return "Invalid input"
        
    def to_base64(self, text : str) -> str:
        try :
            return base64.b64encode(text.encode("ascii"))
        except :
            return "Invalid input"

    def to_hex(self, text : str) -> str:
        try :
            return text.encode("ascii").hex()
        except :
            return "Invalid input"

    def to_binary(self, text : str) -> str:
        try :
            return " ".join([bin(ord(character))[2:] for character in text])
        except :
            return "Invalid input"

    def to_octal(self, text : str) -> str:
        try :
            return " ".join([oct(ord(character))[2:] for character in text])
        except :
            return "Invalid input"

    def to_decimal(self, text : str) -> str:
        try :
            return " ".join([str(ord(character)) for character in text])
        except :
            return "Invalid input"

    def to_morse(self, english_plain_text : str) -> str:
        try :
            return " ".join([dict_char_to_morse[char.upper()] if char != " " else " " for char in english_plain_text])
        except :
            return "Invalid input"

    # Exécute chaque fonction et stocke le résultat dans un fichier texte
    def main(self, text : str) -> str:
        with open("../output.txt", "a", encoding="utf-8") as file :
            file.write(f"Input : {text} \n")
        for function in [self.to_ascii, self.to_base64, self.to_hex, self.to_binary, self.to_octal, self.to_decimal, self.to_morse]:
            print(f"{function} : {function(text)}")
            with open("../output.txt", "a", encoding="utf-8") as file:
                file.write(f"{function} : {function(text)} \n")

if __name__ == "__main__":
    # Tant que l'utilisateur ne quitte pas le programme, on lui demande un texte à convertir
    while True :
        text = input("Enter a text to convert : ")
        if text == "quit" :
            break
        Machina(text)