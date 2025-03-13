class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o Motor")

    def __str__(self):
        return f"{self.__class__.__name__}:{','.join([f'{chave}={valor}'for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
        
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} Estou carregado")

moto = Motocicleta("branca", "abc-1234", 2)
moto.ligar_motor()

carro = Carro("preto", "esd-4321", 4)
carro.ligar_motor()

caminhao = Caminhao("azul", "nmd-3245", 8, True)
caminhao.ligar_motor()

print(moto)
print(carro)
print(caminhao)
        