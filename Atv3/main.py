from exercicio_03 import activityNotifications

def testar_exercicio_03():
    print("📘 Exercício 03 – Notificações de Gastos Suspeitos")
    gastos = [2, 3, 4, 2, 3, 6, 8, 4, 5]
    d = 5
    resultado = activityNotifications(gastos, d)
    print(f"Esperado: 2, Obtido: {resultado}\n")

testar_exercicio_03()