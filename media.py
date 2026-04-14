def calcular_media(p1, p2, ac):
    media = (p1 * 0.4) + (p2 * 0.4) + (ac * 0.2)
    return media


# entrada de dados
p1 = float(input("Nota da Prova 1: "))
p2 = float(input("Nota da Prova 2: "))
ac = float(input("Nota da AC: "))

# cálculo
media = calcular_media(p1, p2, ac)

# resultado
print(f"\nMédia final: {media:.2f}")

if media >= 7:
    print("✅ Aprovado")
else:
    print("❌ Reprovado")