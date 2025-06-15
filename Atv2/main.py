from exercicio_02 import gcbr_insertion_sort

def testar_exercicio_02():
    print("📘 Exercício 02 – Insertion Sort com Deslocamentos")
    casos = [
        [1, 1, 1, 2, 2],
        [2, 1, 3, 1, 2]
    ]
    esperados = [0, 4]
    for i, vetor in enumerate(casos):
        resultado = gcbr_insertion_sort(vetor[:])
        print(f"Teste {i+1} ➜ Esperado: {esperados[i]}, Obtido: {resultado}")
    print()

testar_exercicio_02()