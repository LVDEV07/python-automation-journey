produto = input("Digite o nome do produto: ").upper()
valor = input("Digite um preço: ")
valor = valor.replace("R$", "").replace(".", "").replace(",", ".").strip()
valor_real = float(valor)

qtd = int(input("Digite a quantidade: "))

total = valor_real*qtd

print(f'nome: {produto} valor: {valor_real}, quantidade: {qtd}, valor total: {total:.2f}, frete: {"Gratis" if total>200 else "R$ 19,90"}')


