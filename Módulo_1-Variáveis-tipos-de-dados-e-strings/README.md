# Módulo 1: Variáveis, Tipos de Dados e Strings

### O que é e por que importa

Uma **variável** é um nome dado a um valor para reutilizá-lo depois. O **tipo** define o que esse valor é e o que pode ser feito com ele: não é possível, por exemplo, somar um número com um texto sem conversão.

Isso é essencial para automação: em web scraping, quase todo dado chega como **texto** (preço, data, nome). Sem saber limpar e converter strings, não é possível calcular, comparar ou salvar nada corretamente.

### Como funciona

- Variável é uma **etiqueta**, não uma caixa: `preco = 10` cola o nome `preco` no valor `10` na memória. O Python é *dinamicamente tipado*: o tipo pertence ao valor, não à variável.
- **`input()` sempre retorna `str`**, mesmo que o usuário digite números. É preciso converter com `int()` ou `float()` antes de fazer contas ou comparações.
- **Strings são imutáveis**: métodos como `.upper()` não alteram o texto original, eles criam e retornam um novo texto, que precisa ser guardado em uma variável (`texto = texto.upper()`).
- **f-strings** (`f"Olá, {nome}"`) são a forma moderna de montar textos com variáveis dentro.

Tipos principais:

| Tipo | Exemplo | Uso típico |
|---|---|---|
| `str` | `"Notebook"` | textos, nomes, dados vindos de sites |
| `int` | `42` | quantidades, contagens |
| `float` | `1299.90` | preços, medidas |
| `bool` | `True` / `False` | resultado de comparações |

### Armadilhas comuns

1. **Somar texto com número** (`"Idade: " + 28`) → `TypeError`. Use f-string em vez de concatenação direta.
2. **Esquecer que `input()` retorna texto** → `"10" + "5"` gera `"105"`, não `15`.
3. **Comparar strings numéricas sem converter** → `"10" < "9"` é `True`, porque a comparação é feita **caractere por caractere** pelo código Unicode de cada caractere, não pelo valor numérico. O primeiro caractere `'1'` (código 49) já é menor que `'9'` (código 57), então a comparação para aí.
4. **Achar que um método altera a string original** → strings são imutáveis; sempre reatribuir o resultado.
5. **Converter texto com formato errado** (`float("1.299,90")`) → `ValueError`. É preciso limpar separadores de milhar e trocar vírgula por ponto antes de converter.

### Exercícios

- **Fixação conceitual:** por que `input()` traz problemas em contas e o que resolve isso; o que significa "strings imutáveis"; diferença entre comparação de strings numéricas e números de fato.
- **Desafio prático:** programa que lê nome e preço de um produto em formato brasileiro (`R$ 89,90`), limpa e converte para `float`, lê a quantidade, calcula o total e aplica regra de frete grátis acima de R$ 200.
- **Reflexão aplicada:** situações reais de dados "sujos" (datas, valores, nomes em formatos diferentes) e como a limpeza/conversão de tipos ajudaria a automatizar esse tratamento.