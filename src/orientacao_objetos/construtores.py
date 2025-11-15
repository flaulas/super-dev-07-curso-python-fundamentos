class Cachorro:
    # Construtor com 4 parâmetros (3 parâmetros sem valor default e 1 com valor default)
    def __init__(self, raca_param: str, peso: float, idade: int, cor: str = "Caramelo"):
        # Atributos são preenchidos com os dados dos parâmetros
        # O parâmetro cor tem um valor default(padrão) que é "Caramelo"
        self.raca = raca_param
        self.peso = peso
        self.idade = idade
        self.cor = cor
        # Atributo com valor pré-definido
        self.cidade_natal = "Blumenau"


def exemplo_construtor_cachorro():
    # Cachorro(raca, peso, idade)
    tobby = Cachorro("Dobberman", 45.20, 15, "Preto")
    print("raça:", tobby.raca)
    print("peso:", tobby.peso)
    print("idade:", tobby.idade)
    print("cidade natal:", tobby.cidade_natal)
    print("cor:", tobby.cor)

    # Instanciar um objeto chamado 'daschund' da classe Cachorro
    daschund = Cachorro("Salsicha", 70.00, 5)
    print("raça:", daschund.raca)
    print("peso:", daschund.peso)
    print("idade:", daschund.idade)
    print("cidade natal:", daschund.cidade_natal)
    print("cor:", daschund.cor)


exemplo_construtor_cachorro()


# -------------------------------------------------------------------------------------------
# Exercício de Construtores
# Criar uma classe chamada Passagem com um construtor que contenha os parâmetros abaixo:
# - destino
# - quantidade dias
# - data inicio
# Instanciar dois objetos para desinos diferentes, preenchendo os parâmetros
# Apresentar os dados em uma tabela
# Adicionar os parâmetros abaixo no construtor da classe Passagem
# - quantidade pessoas com valor default 2
# - partida çom valor default 'São Paulo'
# Instanciar outro objeto passando: destino, qtd dias, data inicio, quantidade pessoas
# Apresentar na tabela tbm o novo objeto
# Instanciar outro objeto passando: destino, qtd dias, data inicio, quantidade pessoas, partida
# Apresentar na tabela tbm o novo objeto
