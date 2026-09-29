funcionarios = [
    {"nome": "Ana", "salario": 4500},
    {"nome": "Bruno", "salario": 3200},
    {"nome": "Carla", "salario": 5800},
    {"nome": "Diego", "salario": 2900},
    {"nome": "Elisa", "salario": 6100},
]

menorParaMaior = sorted(funcionarios, key= lambda v:v["salario"])
menoresSalarios = menorParaMaior[:2]

print("Menor salario é de:", menoresSalarios[0]["nome"])
print("O 2° menor salario é de:", menoresSalarios[1]["nome"])

