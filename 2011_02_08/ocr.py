def ocr(numero):
    numeros = {
        '\n   \n   |\n   |\n': 1,
        '\n __\n __|\n|__\n': 2,
        '\n __\n __|\n __|\n': 3,
        '\n\n|__|\n   |\n': 4,
        '\n __\n|__\n __|\n': 5,
        '\n __\n|__  \n|__|\n': 6,
        '\n __\n   |\n   |\n': 7,
        '\n __\n|__|\n|__|\n': 8,
        '\n __\n|__|\n __|\n': 9,
        '\n __\n|  |\n|__|\n': 0,
        '\n      __\n   | |  |\n   | |__|\n':10
        
    }
    return numeros.get(numero, None)
