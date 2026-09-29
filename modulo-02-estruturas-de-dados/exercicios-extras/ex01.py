produtos = [
    {"nome": "Mouse", "preco": 89.90},
    {"nome": "Teclado", "preco": 129.90},
    {"nome": "Monitor", "preco": 749.90},
    {"nome": "Headset", "preco": 199.90},
]

ultimoProduto = produtos[-1]


produtoMaisCaro = max(produtos, key=lambda p:p["preco"])

print("Produto mais caro:",produtoMaisCaro)
print("Nome do produto mais caro ->", produtoMaisCaro["nome"])

print()

print("Ultimo produto:", ultimoProduto)
print("Nome do ultimo produto -> ", ultimoProduto["nome"])
