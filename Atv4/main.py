from exercicio_04 import countRecognizedStrings

def testar_exercicio_04():
    print("📘 Exercício 04 – Cadeias Reconhecidas por Regex")
    casos = [
        ("((ab)|(ba))", 2, 2),
        ("((a|b)*)", 5, 32),
        ("((a*)(b(a*)))", 100, 100)
    ]
    for i, (regex, L, esperado) in enumerate(casos, 1):
        resultado = countRecognizedStrings(regex, L)
        print(f"Teste {i} ➜ Esperado: {esperado}, Obtido: {resultado}")
    print()

testar_exercicio_04()