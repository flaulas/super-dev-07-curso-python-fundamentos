


# -------------------------------- Exemplo de Cálculo de compra no Paraguai ----------------
# Cenário 1: Utilizado a cota de $500 mensal
# comprou o iPhone 17 Pro Max 512GB $ 2000
# Dolar hoje: R$ 5,45
# iPhone base => $ 2000 * R$ 5,45 => R$ 10900
# Valor para calcular o imposto: $2000 - $500 => $1500 (valor utilizado para calcular o imposto)
# 50% do valor em dolar => $1500 * 0.50 => $750
# calcular o valor do imposto => $750 * R$ 5,45 => R$ 4087,50
# total: 4087,50 + R$ 10900 => R$ 14.987,5

# Cenário 2: Utilizado a cota de $500 mensal
# comprou o iPhone 17 Pro Max 512GB $ 2000
# Dolar hoje: R$ 5,45
# iPhone base => $ 2000 * R$ 5,45 => R$ 10900
# Valor para calcular o imposto: $2000 (valor utilizado para calcular o imposto)
# 50% do valor em dolar => $2000 * 0.50 => $1000
# calcular o valor do imposto => $1000 * R$ 5,45 => R$ 5450,00
# total: 5450,00 + R$ 10900 => R$ 16350,00

# Cenário 2: Não pagar o imposto
# comprou o iPhone 17 Pro Max 512GB $ 2000
# Dolar hoje: R$ 5,45
# iPhone base => $ 2000 * R$ 5,45 => R$ 10900
# total: R$ 10900
def solicitar_cotacao_dolar() -> float:
    return 5.45
    cotacao : float = float(input("Digite o valor da cotação do dolar hoje: ").replace(",", "."))
    return cotacao
    # return 5.45


def solicitar_nome_produto() -> str:
    nome = input("Digite o nome do produto: ")
    return nome


def solicitar_valor_produto_dolar() -> float:
    return float(input("Digite o valor do produto em dolar: "))


def solicitar_se_pagara_imposto() -> bool:
    pagar_imposto = input('Pagar imposto? [s/n] ')
    if pagar_imposto == "s":
        return True
    else:
        return False


def solicitar_deseja_utilizar_cota_dolar_mensal() -> bool:
    cota_mensal = input('Utilizar cota mensal? [s/n] ')
    if cota_mensal == "s":
        return True
    else:
        return False
    

def calcular_valor_produto_acrescentando_imposto_utilizando_cota(
    valor_produto_dolar: float,
    cotacao_dolar: float,
    valor_produto_reais: float
):
    cotacao_mensal = 500.00
    # Calcular o valor que será utilizado para descobrir quanto a mais será pago de imposto
    valor_imposto_dolar = (valor_produto_dolar - cotacao_mensal) / 2
    valor_imposto_reais = valor_imposto_dolar * cotacao_dolar

    valor_total_produto_reais = valor_produto_reais + valor_imposto_reais
    print(f"""Valor total do produto: $ {valor_produto_dolar}
Valor total do produto: R$ {valor_produto_reais}
Valor imposto: R$ {valor_imposto_reais}

Valor total do produto com imposto: R$ {valor_total_produto_reais} """)

# Ex.1 : Criar uma função chamada exercicio_aluno
# Solicitar o nome (criar função)
# Solicitar o nota 1 (criar função)
# Solicitar o nota 2 (criar função)
# Solicitar o nota 3 (criar função)
# Calcular a média e apresentar
# Criar um if que verifique se o aluno está ou não aprovado e apresentar
# Solicitar a idade (criar função)
# Solicitar o peso (criar função)
# Solicitar a altura (criar função)
# Calcular o imc do aluno e apresentar a classificação
# Apresentar a geração de acordo com a idade
# Solicitar o cargo (criar função)
# Apresentar salário de acordo com cargo
#   Estagiário R$ 850,00
#   Junior R$ 1800,00
#   Pleno R$ 4000,00
#   Senior R$ 6000,00


def calcular_valor_produto_acrescentando_imposto(
    valor_produto_dolar: float,
    cotacao_dolar: float,
    valor_produto_reais: float,
):
    valor_imposto_dolar = valor_produto_dolar / 2 # 50% de imposto
    valor_imposto_reais = valor_imposto_dolar * cotacao_dolar

    valor_total_produto_reais = valor_produto_reais + valor_imposto_reais
    print("Valor total do produto com imposto: " + str(valor_total_produto_reais))


def calcular_valor_compra_paraguai():
    cotacao_dolar: float = solicitar_cotacao_dolar()
    nome_produto: str = solicitar_nome_produto()
    valor_produto_dolar : float = solicitar_valor_produto_dolar()
    pagara_imposto : bool = solicitar_se_pagara_imposto()
    # Calcular o valor do produto em reais
    valor_produto_reais = valor_produto_dolar * cotacao_dolar

    if pagara_imposto == True:
        utilizar_cota_dolar_mensal = solicitar_deseja_utilizar_cota_dolar_mensal()

        # Descobrir o valor do produto para calcular o imposto
        if utilizar_cota_dolar_mensal == True:
            calcular_valor_produto_acrescentando_imposto_utilizando_cota(
                valor_produto_dolar, cotacao_dolar, valor_produto_reais,
            )
        else:
            calcular_valor_produto_acrescentando_imposto(
                valor_produto_dolar, cotacao_dolar, valor_produto_reais,
            )
    else:
        print("Valor do produto sem pagar imposto: " + str(valor_produto_reais))


        