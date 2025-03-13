class Cachorro:
    def __init__(self, name, cor, acordado=True):
        print("Iniciando classe...")

        self.name = name
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo o instanciamento da classe...")

    def latir(self):
        print("Au Au")

def criar_cachorro():
    c1 = Cachorro("Tunico", "Preto")
    print(c1.name)

c2 = Cachorro("Kiara", "Amarela")

c2.latir()

print("Vou destruir a instancia")

print("Ainda não destrui")

del c2

print("Agora destrui")

#criar_cachorro()

