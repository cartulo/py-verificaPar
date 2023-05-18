# -*- coding: utf-8 -*-
import math
try:
    numero = float(input("Digite um número: "))

    if numero >= 0:
        raiz = math.sqrt(numero)
        print("================================================")
        print("A raíz quadrada vale: {}".format(raiz))
        print("================================================")
        input("Pressione qualquer tecla para sair.")

    else:
        print("================================================")
        print("Número inserido é inválido.")
        print("================================================")
        input("Pressione qualquer tecla para sair.")

except (TypeError, NameError, SyntaxError, ValueError):
    print("================================================")
    print("Apenas números são aceitos")
    print("================================================")
    input("Pressione qualquer tecla para sair.")