'''7 – Implemente um programa para calcular sua média final em uma determinada unidade
curricular. O programa deve solicitar ao usuário a quantidade de notas, o valor para cada
uma das notas e exibir, ao final, a média aritmética simples e informar se o(a) estudante
está Aprovado ou Reprovado. Considere que a média mínima para a aprovação é 6.'''

qnt_nota = int(input("Digite a quantidade de notas: "))

soma = 0

for i in range(1, qnt_nota + 1):
    nota = float(input(f"Digite a nota {i}: "))
    soma = soma + nota

media = soma / qnt_nota

print(f"\nMédia final: {media:.2f}")    # \n significa quebrar a linha, ele escreve a media em duas linhas
# {media} → valor da variável, : começa a formatação, .2f → número com 2 casas decimais (float)

if media >= 6:
    print("Status: Aprovado")
else:
    print("Status: Reprovado")