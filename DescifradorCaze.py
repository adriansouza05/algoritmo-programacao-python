# descriptografia.py
# Módulo B - Decifrar mensagem RSA
# Cesar e Victor
# Chaves: n = 3233, d = 2753

# ===================================================
# descriptografa um bloco: M = C^d mod n
# ===================================================
def decrypt(cifra, chave_privada):
    n, d = chave_privada

    # pow(cifra, d, n) faz a mesma coisa que (cifra ** d) % n
    # mas muito mais rápido e sem estourar memória
    # em C a gente precisava do Big Int pra isso, aqui o python já resolve sozinho
    return pow(cifra, d, n)


# ===================================================
# cuida da lista inteira, descriptografando caractere por caractere
# ===================================================
def descriptografar_mensagem(lista_cifras, chave_privada):
    resultado = ""

    for cifra in lista_cifras:
        numero = decrypt(cifra, chave_privada)

        # chr() é o inverso do ord() que a outra dupla usou no sistema de cifrar
        # ord('A') = 65 → cifra → decrypt = 65 → chr(65) = 'A'
        resultado += chr(numero)

    return resultado


# ===================================================
# função principal
# ===================================================
def executar_modulo_b():
    print("=== MÓDULO B: DECIFRAR ===")

    try:
        # valores comentados la em cima
        n = int(input("Digite o módulo 'n' da chave privada: "))
        d = int(input("Digite o expoente 'd' da chave privada: "))
        chave_privada = (n, d)

        # a outra dupla vai entregar a lista tipo [1234, 5678, 910]
        entrada = input("Cole a mensagem cifrada (ex: [1234, 5678, ...]): ")

#Nessa parte tive de entender como funciona os metodos, pra facilitar a leitura e remover os espcos e demais caracteres indesejaveis utilizei:
# https://youtu.be/qJqoUMedgNI?si=n-AkC8fDtWNCXauW

        # remove espaços das pontas, depois remove os colchetes [ ]
        entrada = entrada.strip().removeprefix('[').removesuffix(']')

        # corta na vírgula e converte cada pedaço pra inteiro
        lista_cifras = [int(x.strip()) for x in entrada.split(',')]

        print(f"\nDetectado: {len(lista_cifras)} caracteres cifrados")
        print("Processando decifragem...")

        texto_claro = descriptografar_mensagem(lista_cifras, chave_privada)

        print("\n--- RESULTADO ---")
        print(f"Mensagem original: {texto_claro}")
        print("-----------------")

    except ValueError:
        print("Erro: verifique se a lista e as chaves estão corretas.")
    except Exception as erro:
        print(f"Erro inesperado: {erro}")


# roda só se executar esse arquivo diretamente
if __name__ == "__main__":
    executar_modulo_b()