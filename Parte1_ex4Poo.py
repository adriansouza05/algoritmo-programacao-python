alunos = [
{"nome": "Ana", "media": 7.5} ,
{"nome": "Bruno", "media": 5.0} ,
{"nome": "Carla", "media": 8.2}
]

lista_aprovados = []

for i in alunos:
    if i["media"] >= 6:
        lista_aprovados.append(i["nome"])

print("\nAlunos aprovados com media maior ou igual a 6:")
print(f"{lista_aprovados}\n")


nova_lista = [ i for i in alunos if i["media"] >= 7 ]

print("Alunos aprovados com media maior ou igual a 7:")
print(f"{nova_lista}\n")