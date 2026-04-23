notas = [7.5, 8.0, 6.0, 9.0, 5.5]

media = sum(notas) / len(notas)
maior = max(notas)
menor = min(notas)

aprovados = len([n for n in notas if n >= 7])
reprovados = len([n for n in notas if n < 7])

print("RELATÓRIO")
print(f"Notas: {notas}")
print(f"Média: {media:.2f}")
print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")
print(f"Aprovados: {aprovados}")
print(f"Reprovados: {reprovados}")
