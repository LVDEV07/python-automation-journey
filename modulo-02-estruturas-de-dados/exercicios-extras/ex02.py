vendas = [150.00, 320.50, 89.90, 450.00, 199.00, 275.30]

valores = vendas[:3]

maior = max(valores)

print("Tres primeiros valores", valores)
#Não funcionaria em uma lista de dicionarios pois o max tentaria comparar os dicionarios e nao os valores dentro dele
print("maior valor", maior)

