produtos = [
    {"nome": "Fone Bluetooth", "preco": 129.90, "categoria": "áudio"},
    {"nome": "Caixa de Som", "preco": 199.90, "categoria": "áudio"},
    {"nome": "Webcam HD", "preco": 159.90, "categoria": "informática"},
    {"nome": "Microfone USB", "preco": 249.90, "categoria": "áudio"},
    {"nome": "Suporte Notebook", "preco": 79.90, "categoria": "informática"},
]

nomes = [p["nome"] for p in produtos if p["categoria"] == "áudio"]

print(f"Quantidade de produtos:  {len(produtos)} \nProdutos: ",*("\n" + n for n in nomes))


precoMedio = sum(n["preco"] for n in produtos)/len(produtos)

print(f"Preco medio: {precoMedio:.2f}")

categoriasUnicas = set(c["categoria"] for c in produtos)

print(f"Categorias unicas: ", *("\n" + c for c in categoriasUnicas))

# key=lambda p: p["preco"] diz ao min() para comparar os dicionários
# pelo campo "preco", em vez de tentar comparar os dicionários inteiros
# (o que geraria erro). Retorna o dicionário completo com o menor preço.
maisBarato = min(produtos, key=lambda p : p["preco"])
print(f"Produto mais barato: {maisBarato["nome"]}, R${maisBarato["preco"]:.2f}")


