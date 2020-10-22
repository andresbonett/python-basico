# Palindromo

def palindromo(palabra):
  palabra = palabra.replace(' ', '').lower()
  palabra_invertida = palabra[::-1]
  if palabra_invertida == palabra:
    return True
  else:
    return False


def run():
  palabra = input("Ingrese una palabra o frase para comprobar si es Palindromo: ")
  es_palindromo = palindromo(palabra)
  if es_palindromo:
    print("Es Palindromo")
  else:
    print("No es Palindromo")


if __name__ == "__main__":
  run()