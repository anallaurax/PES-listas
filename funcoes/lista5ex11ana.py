'''11 – Crie um algoritmo com uma função que retorna um valor em reais escrito por extenso.
Por exemplo, caso seja passado “1.74” como parâmetro para a função, ela deve retornar:
um real e setenta e quatro centavos. Caso seja passado “3251.90”, deve retornar
“três mil duzentos e cinquenta e um reais e noventa centavos”.'''

def numero_por_extenso(numero):
    unidades = [
        "zero", "um", "dois", "três", "quatro",
        "cinco", "seis", "sete", "oito", "nove"
    ]

    especiais = {
        10: "dez",
        11: "onze",
        12: "doze",
        13: "treze",
        14: "quatorze",
        15: "quinze",
        16: "dezesseis",
        17: "dezessete",
        18: "dezoito",
        19: "dezenove"
    }

    dezenas = {
        20: "vinte",
        30: "trinta",
        40: "quarenta",
        50: "cinquenta",
        60: "sessenta",
        70: "setenta",
        80: "oitenta",
        90: "noventa"
    }

    centenas = {
        100: "cem",
        200: "duzentos",
        300: "trezentos",
        400: "quatrocentos",
        500: "quinhentos",
        600: "seiscentos",
        700: "setecentos",
        800: "oitocentos",
        900: "novecentos"
    }

    if numero < 10:
        return unidades[numero]

    if numero < 20:
        return especiais[numero]

    if numero < 100:
        dezena = numero - numero % 10
        unidade = numero % 10

        if unidade == 0:
            return dezenas[dezena]

        return dezenas[dezena] + " e " + unidades[unidade]

    if numero < 1000:
        centena = numero - numero % 100
        resto = numero % 100

        if resto == 0:
            return centenas[centena]

        if resto < 10:
            return centenas[centena] + " e " + unidades[resto]

        return centenas[centena] + " e " + numero_por_extenso(resto)

    if numero < 2000:
        resto = numero - 1000

        if resto == 0:
            return "mil"

        return "mil " + numero_por_extenso(resto)

    if numero < 10000:
        milhar = numero // 1000
        resto = numero % 1000

        resultado = numero_por_extenso(milhar) + " mil"

        if resto == 0:
            return resultado

        return resultado + " " + numero_por_extenso(resto)


def valor_por_extenso(valor):
    valor = float(valor)

    reais = int(valor)
    centavos = round((valor - reais) * 100)

    if reais == 1:
        resultado = "um real"
    else:
        resultado = numero_por_extenso(reais) + " reais"

    if centavos > 0:
        resultado += " e "

        if centavos == 1:
            resultado += "um centavo"
        else:
            resultado += numero_por_extenso(centavos) + " centavos"

    return resultado


valor = input("Digite um valor em reais: ")

print(valor_por_extenso(valor))