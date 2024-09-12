from Veiculo import Veiculo
class Caminhao(Veiculo):
    def __init__(self, marca, modelo, placa, ano, capacidade):
        super().__init__(marca, modelo, placa, ano)
        self.__capacidade = capacidade
    #Override - Sobrescrever o método __str__()
    def __str__(self):
        retorno2 = super().__str__()
        return f'''{retorno2}
- Capacidade: {self.__capacidade}'''