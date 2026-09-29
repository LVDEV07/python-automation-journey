produtos = [
    {"nome": "Mouse", "preco": 89.90, "categoria": "informática"},
    {"nome": "Sofá", "preco": 1899.00, "categoria": "móveis"},
    {"nome": "Teclado", "preco": 129.90, "categoria": "informática"},
    {"nome": "Cadeira", "preco": 899.00, "categoria": "móveis"},
    {"nome": "Webcam", "preco": 159.90, "categoria": "informática"},
    {"nome": "Mesa", "preco": 650.00, "categoria": "móveis"},
]

produtosInformatica = [i for i in produtos if i["categoria"] == "informática"]

maisCaroParaMaisBarato = sorted(produtosInformatica, key=lambda p:p["preco"], reverse=True)

doisPrimeiros = maisCaroParaMaisBarato[:2]

for i in doisPrimeiros:
    print(f"Nome: {i["nome"]} Preco: {i["preco"]} \n")