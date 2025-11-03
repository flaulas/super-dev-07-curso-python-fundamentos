# pip install streamlit
# py -m pip install streamlit

# para exeuctar : streamlit run arquivo.py
import streamlit as st

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
    st.write(f"""Valor total do produto: $ {valor_produto_dolar}
Valor total do produto: R$ {valor_produto_reais}
Valor imposto: R$ {valor_imposto_reais}

Valor total do produto com imposto: R$ {valor_total_produto_reais} """)
    

def calcular_valor_produto_acrescentando_imposto(
    valor_produto_dolar: float,
    cotacao_dolar: float,
    valor_produto_reais: float,
):
    valor_imposto_dolar = valor_produto_dolar / 2 # 50% de imposto
    valor_imposto_reais = valor_imposto_dolar * cotacao_dolar

    valor_total_produto_reais = valor_produto_reais + valor_imposto_reais
    st.write("Valor total do produto com imposto: " + str(valor_total_produto_reais))
    

def calcular_valor_compra_paraguai():
    # Calcular o valor do produto em reais
    valor_produto_reais = valor_produto_dolar * cotacao_dolar

    if pagar_imposto == True:
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
        st.write("Valor do produto sem pagar imposto: " + str(valor_produto_reais))


st.write("Calculador Paraguai")

nome = st.text_input("Nome")
cotacao_dolar = st.number_input("Cotação do dolar")
valor_produto_dolar = st.number_input("Valor produto em dolar")

pagar_imposto = st.toggle("Pagar imposto")
utilizar_cota_dolar_mensal = False
if pagar_imposto:
    utilizar_cota_dolar_mensal = st.toggle("Utilizar cota")
botao_calcular = st.button("Calcular", type="primary")

if botao_calcular:
    calcular_valor_compra_paraguai()