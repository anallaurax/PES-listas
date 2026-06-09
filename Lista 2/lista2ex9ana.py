'''9 – Considere que você deseja fazer uma reserva mensal, em dinheiro, para a compra de
um determinado presente para você mesmo(a). Considere que todo mês você depositará,
em uma poupança no banco, um mesmo valor em reais. Faça um programa que leia o
valor que será depositado mensalmente e exiba na tela o valor acumulado mês a mês
durante 24 meses. Considere que a taxa de juros de uma poupança é 0,5% ao mês, que
a poupança não possui nenhum saldo inicial. Você pode utilizar uma calculadora de juros
compostos para validar o cálculo do seu algoritmo, por exemplo o site: '''

valor = float(input("Digite o valor que será guardado:"))
qnt_meses = int(input("Informe a quantidade de meses que voce irá guardar o dinheiro:"))
juros = 0.005

valor_acumulado = 0

for mes in range(1, qnt_meses + 1):
    # Cada mês depositamos o valor e aplicamos os juros sobre o total acumulado
    valor_acumulado = (valor_acumulado + valor) * (1 + juros)
    print(f"Mês {mes}: R$ {valor_acumulado:.2f}")