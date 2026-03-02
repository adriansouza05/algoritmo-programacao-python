while True:
    num = int(input("Digite um número (0 para sair): "))

    if num == 0:
        break

    if num % 2 == 0:
        print("É par!")
    else:
        print("É ímpar!")