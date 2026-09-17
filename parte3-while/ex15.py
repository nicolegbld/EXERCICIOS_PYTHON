
positivo = 0

while True:
    if numero > 0:
        positivo += 1 
    elif numero == 0:
        break

    numero = float(input("Informe um número(0 para parar): "))
    print("Quantidade de números positivos: " , positivo)

    