import sympy
import math


def validar_primo(numero):
    """Verifica se um número é primo"""
    return sympy.isprime(numero)


def gerar_chaves(p, q):
    """Gera as chaves pública e privada RSA"""

    n = p * q
    phi = (p - 1) * (q - 1)

    # Expoente público padrão
    e = 65537

    # Garante que e seja coprimo com phi
    if math.gcd(e, phi) != 1:
        e = 3
        while math.gcd(e, phi) != 1:
            e += 2

    # Calcula o inverso modular
    d = pow(e, -1, phi)

    return (n, e), (n, d)


def criptografar_mensagem(mensagem, chave_publica):
    """Criptografa caractere por caractere"""

    n, e = chave_publica
    lista_cifrada = []

    for caractere in mensagem:
        valor_ascii = ord(caractere)

        # RSA: c = m^e mod n
        cifra = pow(valor_ascii, e, n)

        lista_cifrada.append(cifra)

    return lista_cifrada


def main():

    print("=" * 60)
    print("CRIPTOGRAFIA RSA")
    print("=" * 60)

    try:
        print("\nInforme dois números primos diferentes:")

        p = int(input("Digite o primeiro primo (p): "))
        q = int(input("Digite o segundo primo (q): "))

    except ValueError:
        print("\nERRO: Digite apenas números inteiros.")
        return

    # Validação dos primos
    if not validar_primo(p):
        print(f"\nERRO: {p} não é primo.")
        return

    if not validar_primo(q):
        print(f"\nERRO: {q} não é primo.")
        return

    if p == q:
        print("\nERRO: p e q não podem ser iguais.")
        return

    print("\n✓ Números primos válidos")

    # Geração das chaves
    chave_publica, chave_privada = gerar_chaves(p, q)

    n, e = chave_publica
    _, d = chave_privada

    print("\n" + "-" * 60)
    print("CHAVES GERADAS:")
    print("-" * 60)

    print(f"Chave Pública (n, e): ({n}, {e})")
    print(f"Chave Privada (n, d): ({n}, {d})")

    print("\n⚠️ Guarde a chave privada!")

    # Mensagem
    mensagem = input(
        "\nDigite a mensagem para criptografar: "
    )

    # Criptografia
    lista_cifrada = criptografar_mensagem(
        mensagem,
        chave_publica
    )

    print("\n" + "-" * 60)
    print("MENSAGEM CRIPTOGRAFADA")
    print("-" * 60)
    print(lista_cifrada)
    print("-" * 60)


if __name__ == "__main__":
    main()