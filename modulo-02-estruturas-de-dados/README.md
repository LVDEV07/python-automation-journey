# Módulo 2: Estruturas de Dados

### O que é e por que importa

Estruturas de dados são formas de organizar múltiplos valores sob uma única variável. Até o Módulo 1, cada variável guardava um valor por vez; aqui o foco passa a ser guardar **coleções** de valores: uma lista de produtos, um dicionário com os dados de um produto, um conjunto de categorias sem repetição.

Isso é o núcleo de qualquer automação real. Um scraping não traz "um preço", ele traz uma **lista** de dezenas de produtos, cada um representado por um **dicionário**, exatamente o formato que APIs devolvem em JSON. Sem dominar essas estruturas, não é possível processar dados em lote.

### Como funciona

| Estrutura | Sintaxe | Característica principal | Uso típico |
|---|---|---|---|
| Lista (`list`) | `[1, 2, 3]` | Ordenada, mutável, permite repetição | Coleção de produtos coletados |
| Tupla (`tuple`) | `(1, 2, 3)` | Ordenada, imutável | Coordenadas, dados fixos que não devem mudar por acidente |
| Dicionário (`dict`) | `{"chave": "valor"}` | Pares chave-valor | Um produto com nome, preço, link, igual JSON de API |
| Set (`set`) | `{1, 2, 3}` | Não ordenado, não permite repetição | Remover duplicatas, checar existência rápido |

Conceitos-chave:

- **Indexação e fatiamento (slicing):** listas e tuplas são acessadas por posição, começando em `0`. `lista[0]` é o primeiro item, `lista[-1]` é o último, `lista[1:3]` pega do índice 1 até o 2.
- **Dicionário usa chave, não índice numérico:** `produto["preco"]`, não `produto[0]`. É assim que dados de API/JSON chegam.
- **Mutabilidade:** listas e dicionários podem ser alterados depois de criados (`.append()`, `["chave"] = novo_valor`). Tuplas não podem ser alteradas depois de criadas, por isso guardam dados que precisam permanecer fixos durante a execução.
- **List comprehension:** forma compacta de criar uma lista a partir de outra, aplicando transformação ou filtro em uma linha: `[x*2 for x in lista]`.
- **`key=lambda`** em `max()`, `min()` e `sorted()`: diz por qual campo comparar itens complexos como dicionários, já que o Python não sabe comparar dois dicionários diretamente. `max(produtos, key=lambda p: p["preco"])` encontra o dicionário com o maior valor no campo `"preco"`.

### Armadilhas comuns

1. **Confundir lista com dicionário na hora de acessar:** `produto[0]` num dicionário dá `KeyError`. Dicionário se acessa por chave, lista por posição.
2. **Acessar índice que não existe:** `produtos[10]` numa lista de 3 itens gera `IndexError`. Sempre conferir o tamanho com `len()` antes.
3. **Tentar alterar uma tupla:** `tupla[0] = 99` gera `TypeError`, porque tuplas não têm suporte a atribuição por índice.
4. **Modificar uma lista enquanto percorre ela com `for`:** remover itens de uma lista dentro do próprio loop pula elementos. Prefira criar uma lista nova com list comprehension.
5. **Achar que dicionário mantém posição 0, 1, 2:** dicionários são organizados por chave; não existe `dicionario[0]` a menos que `0` seja literalmente uma chave.

### Exercícios

- **Fixação conceitual:** diferença entre lista e tupla e quando escolher cada uma; por que `set` é útil para remover duplicatas; comportamento de fatiamento e de acesso a índice fora do intervalo em uma lista.
- **Desafio prático:** a partir de uma lista de produtos coletados por scraping (lista de dicionários), calcular quantidade total, filtrar por categoria com list comprehension, calcular preço médio, extrair categorias únicas com `set` e encontrar o produto mais barato sem usar índices fixos.
- **Reflexão aplicada:** identificar, num robô real que o aluno queira construir, quais dados fariam mais sentido como lista e quais como dicionário.