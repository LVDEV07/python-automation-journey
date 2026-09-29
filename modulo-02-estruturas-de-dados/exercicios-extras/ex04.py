pedidos = [
    {"id": 101, "cliente": "Ana", "total": 320.50},
    {"id": 102, "cliente": "Bruno", "total": 89.90},
    {"id": 103, "cliente": "Carla", "total": 199.00},
    {"id": 104, "cliente": "Diego", "total": 450.00},
    {"id": 105, "cliente": "Elisa", "total": 150.00},
]

menorValor = min(pedidos, key=lambda v:v["total"])

print("menor pedido:", menorValor)

posicao = pedidos.index(menorValor)
print("Index:",posicao)
print("Acessando pelo index: ", pedidos[posicao])


