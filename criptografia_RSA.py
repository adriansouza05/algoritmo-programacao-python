# RSA - Criptografia (Módulo de Encriptação)

def encriptar_rsa(mensagem: str, e: int, n: int) -> list[int]:
    """
    Encripta uma string caractere por caractere usando a chave pública (e, n).
    Retorna uma lista de inteiros que deve ser repassada para a outra dupla.
    """
    cifrado = []  # Lista que armazenará os valores encriptados de cada caractere

    for char in mensagem:
        m = ord(char)  # Converte o caractere para seu valor ASCII (ex: 'A' → 65)

        # Validação: RSA só funciona corretamente se m < n
        # Se m >= n, a operação mod n perde informação e a decriptação falha
        if m >= n:
            raise ValueError(f"O caractere '{char}' (valor {m}) excede o limite do n={n}.")

        # Fórmula central do RSA: c = m^e mod n
        # pow(m, e, n) é equivalente a (m ** e) % n, mas muito mais eficiente
        # pois usa exponenciação modular rápida (não calcula m^e inteiro)
        c = pow(m, e, n)

        cifrado.append(c)  # Adiciona o valor encriptado à lista

    return cifrado  # Cada posição da lista corresponde a um caractere da mensagem original


if __name__ == "__main__":

    # Chave pública (e, n) fornecida pelo enunciado ou combinada com a outra dupla
    # e = expoente público | n = módulo (produto de dois primos p e q)
    e = 17
    n = 3233  # 3233 = 61 × 53 (p e q escolhidos pela dupla de decriptação)

    # Lê a mensagem em texto plano que será encriptada
    texto = input("Digite a mensagem para encriptar: ")

    try:
        texto_cifrado = encriptar_rsa(texto, e, n)

        # Exibe a lista de inteiros encriptados
        # Cada número representa um caractere — sem a chave privada (d, n), é ilegível
        print("\n--- Resultado ---")
        print("Entregue esta lista para a outra dupla:")
        print(texto_cifrado)

    except ValueError as erro:
        # Captura o caso em que algum caractere tem valor ASCII maior ou igual a n
        print(f"\nErro na encriptação: {erro}")