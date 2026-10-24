
def main():
    texto = input("Digite um texto: ")
    print(convert(texto))

def convert(texto):
    return texto.replace(":)", "🙂").replace(":(", "🙁")

main()