respuesta = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
respuesta = respuesta.strip().lower()

if respuesta == "42" or respuesta == "forty-two" or respuesta == "forty two":
    print("Yes")
else:
    print("No")