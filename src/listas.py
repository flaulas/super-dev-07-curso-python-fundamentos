import json
from typing import Dict, List, Union

import questionary
import requests


def exemplo_lista_basica():
    # Criando uma lista de string e armazenando um nome
    nomes: List[str] = ["João"]

    # Acrescentar item na lista
    nomes.append("Maria")

    # Obter o nome da posição zero
    nome_primeira_posicao = nomes[0]

    # Alterar o nome do João que está na primeira posição
    nomes[0] = "João Cleber"

    # Adicionar elemento para depois apagar
    nomes.append("Lúcio")

    # Apagar um elemento da lista
    nomes.remove("Lúcio")

    tamanho_lista = len(nomes)

    print(f"""Primeiro nome: {nomes[0]}
Segundo nome: {nomes[1]}
Tamanho da lista: {tamanho_lista}""")


def exemplo_solicitar_dados_usuario():
    valores = []

    valores.append(float(input("Digite o valor do produto: ")))
    valores.append(float(input("Digite o valor do produto: ")))
    valores.append(float(input("Digite o valor do produto: ")))
    valores.append(float(input("Digite o valor do produto: ")))
    valores.append(float(input("Digite o valor do produto: ")))

    soma = valores[0] + valores[1] + valores[2] + valores[3] + valores[4]

    print(valores)
    print(soma)

def exemplo_solicitar_dados_usuario_otimizado():
    valores = []

    # para i de 0 até 5
    for i in range(0, 5):
        valores.append(float(input("Digite o valor do produto: ")))

    soma = 0
    for i in range(0, 5):
        valor = valores[i]
        soma = soma + valor
    print(f"Soma: {soma}")


def exemplo_lista_com_dicionario():
    # pip install --requirement requirements.txt
    
    # Solicitar cep, valor imóvel, cnpj
    # Fazer requisição para pegar os dados do endereço buscando através do CEP
    # Fazer requisição para pegar os dados da empresa buscando através do CNPJ
    # Cadastrar este imóvel na lsita de imóveis
    # Continuar perguntando até finalizar
    # Salvar em um arquivo json
    # Outro exercício é importar este json

    # 89.070-200 => 89070200
    cep = questionary.text("Digite o CEP").ask().replace(".", "").replace("-", "")
    valor_imovel = float(questionary.text("Digite o valor do imóvel").ask().replace(",", "."))

    print("Consultado dados do CEP")
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code != 200:
        print("Não foi possível consultar os dados do CEP")
        print(f"Mensagem do erro: {response.text}")
        return
    else:
        print("Consulta do CEP realizada com sucesso")
        dados_response = response.json()
        bairro = dados_response.get("bairro")
        logradouro = dados_response.get("logradouro")
        estado = dados_response.get("uf")
        cidade = dados_response.get("localidade")

    imovel : Dict[str, Union[float, Dict[str, str]]] = {
        "valor": valor_imovel,
        "endereco": {
            "cep": cep,
            "bairro": bairro,
            "logradouro": logradouro,
            "estado": estado,
            "cidade": cidade
        }
    }

    print(json.dumps(imovel, indent=4))

