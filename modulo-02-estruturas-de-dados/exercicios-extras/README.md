# Exercícios Extras: Acesso a Listas e key=lambda

Lista de exercícios extras para reforçar acesso a listas (indexação, indexação negativa, fatiamento) combinado com `key=lambda` em `min()`, `max()` e `sorted()`.

## Exercício 1

```python
produtos = [
    {"nome": "Mouse", "preco": 89.90},
    {"nome": "Teclado", "preco": 129.90},
    {"nome": "Monitor", "preco": 749.90},
    {"nome": "Headset", "preco": 199.90},
]
```

a) Pegue o último produto da lista original.
b) Encontre o produto mais caro da lista.
c) Imprima os nomes dos dois.

## Exercício 2

```python
vendas = [150.00, 320.50, 89.90, 450.00, 199.00, 275.30]
```

a) Pegue só as 3 primeiras vendas da lista.
b) Dessas 3, encontre a maior.
c) Explique com suas palavras por que a forma que você resolveu o item (b) funcionaria ou não numa lista de dicionários.

## Exercício 3

```python
funcionarios = [
    {"nome": "Ana", "salario": 4500},
    {"nome": "Bruno", "salario": 3200},
    {"nome": "Carla", "salario": 5800},
    {"nome": "Diego", "salario": 2900},
    {"nome": "Elisa", "salario": 6100},
]
```

a) Ordene a lista do menor para o maior salário.
b) Pegue só os 2 funcionários com menor salário dessa lista ordenada.
c) Imprima o nome de cada um.

## Exercício 4

```python
pedidos = [
    {"id": 101, "cliente": "Ana", "total": 320.50},
    {"id": 102, "cliente": "Bruno", "total": 89.90},
    {"id": 103, "cliente": "Carla", "total": 199.00},
    {"id": 104, "cliente": "Diego", "total": 450.00},
    {"id": 105, "cliente": "Elisa", "total": 150.00},
]
```

a) Encontre o pedido de menor valor.
b) Descubra em que posição da lista original esse pedido está.
c) Confirme acessando a lista original nessa posição e mostre que é o mesmo pedido.

## Exercício 5

```python
produtos = [
    {"nome": "Mouse", "preco": 89.90, "categoria": "informática"},
    {"nome": "Sofá", "preco": 1899.00, "categoria": "móveis"},
    {"nome": "Teclado", "preco": 129.90, "categoria": "informática"},
    {"nome": "Cadeira", "preco": 899.00, "categoria": "móveis"},
    {"nome": "Webcam", "preco": 159.90, "categoria": "informática"},
    {"nome": "Mesa", "preco": 650.00, "categoria": "móveis"},
]
```

a) Separe só os produtos da categoria "informática".
b) Ordene esses produtos do mais caro para o mais barato.
c) Pegue só os 2 primeiros dessa lista ordenada.
d) Imprima o resultado numa f-string: `"1º: Nome (R$ preço) | 2º: Nome (R$ preço)"`.