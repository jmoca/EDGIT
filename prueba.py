frase = "Tal vez descubra la mentira al comparar las mentiras"
frase = frase.split()

for palabra in frase:
    nueva_palabra = palabra[:]
    print(f"Palabra: {nueva_palabra},\n número de letras: {len(nueva_palabra)}")


