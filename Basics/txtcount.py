def txtCount():
    text = str(input('Escribe  una frase  por favor   :'))
    search_text = str(input('escribe la letra que deseas buscar cuantas veces se repite  :'))
    cont_text = text.count(search_text)
    print(cont_text)

if __name__ == '__main__':
    txtCount()