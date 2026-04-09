# Entrada das informações
produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço unitário (ex.: 4.50): "))
quantidade = int(input("Digite a quantidade comprada: "))
# Processamento (realização do cálculo)
total = preco * quantidade
# Saída – Exibindo as informações.
print(f"Você comprou {quantidade}x {produto}(s).")
print(f"Valor total da compra: R$ {total:.2f}")