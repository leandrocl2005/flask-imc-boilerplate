def mainFunction(resp):

    peso = resp.get("peso")  # pega o peso
    altura = resp.get("altura")  # pega a altura (cm)

    peso = float(peso)  # transforma "peso" em float
    altura = float(altura)  # transforma "altura" em float

    altura = altura / 100  # converte em metros

    resultado = peso / (altura * altura)  # calcula o resultado

    resultado = round(resultado, 2)  # arredonda em 2 casas decimais

    return resultado
