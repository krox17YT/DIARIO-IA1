def main():
    input_text = input("Digite um texto: ")
    resultado = convert(input_text)
    print(resultado)

def convert(input_text):
    return input_text.replace(":)", "🙂").replace(":(", "🙁")

main()