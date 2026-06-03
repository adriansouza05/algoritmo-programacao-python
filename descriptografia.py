def descriptografar_mensagem(
    lista_cifrada,
    chave_privada
):
    """Descriptografa a lista cifrada"""

    n, d = chave_privada
    mensagem = ""

    for cifra in lista_cifrada:

        # RSA: m = c^d mod n
        valor_ascii = pow(cifra, d, n)

        mensagem += chr(valor_ascii)

    return mensagem


def main():

    print("=" * 60)
    print("DESCRIPTOGRAFIA RSA")
    print("=" * 60)

    try:
        print("\nInforme a chave privada:")

        n = int(input("Digite n: "))
        d = int(input("Digite d: "))

    except ValueError:
        print("\nERRO: Digite apenas números inteiros.")
        return

    if n <= 0 or d <= 0:
        print("\nERRO: n e d devem ser positivos.")
        return

    chave_privada = (n, d)

    # Recebe a lista cifrada
    lista_str = input(
        "\nDigite a lista cifrada "
        "(ex: [3065, 3179]): "
    )

    try:
        lista_cifrada = eval(lista_str)

        if not isinstance(lista_cifrada, list):
            raise ValueError

    except:
        print("\nERRO: Lista inválida.")
        return

    # Descriptografia
    try:
        mensagem = descriptografar_mensagem(
            lista_cifrada,
            chave_privada
        )

        print("\n" + "-" * 60)
        print("MENSAGEM ORIGINAL")
        print("-" * 60)
        print(mensagem)
        print("-" * 60)

    except Exception as erro:
        print(
            f"\nERRO ao descriptografar: {erro}"
        )

        
if __name__ == "__main__":
    main()