class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = 1
    
    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta Parada!")

    def correr(self):
        print("Vruuum...")

    def trocar_marcha(self,nro_marcha):
        print("Trocando Marcha")
        def _trocar_marcha(nro_marcha):
            if nro_marcha > self.marcha:
                print("Marcha trocada...")
            else:
                print("Não foi possivel trocar de marcha...")


    #Como alterar a exibição do item de forma hard code:
    #def __str__(self):
     #   return f"Bicicleta: {self.cor}. {self.modelo}, {self.ano}, {self.valor}"
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.
        __dict__.items()])}"

b1 = Bicicleta("vermelha", "caloi", 2022, 600)  
b1.buzinar()
b1.correr()
b1.parar()
b1.trocar_marcha(2)

print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)

Bicicleta.buzinar(b2) # é o mesmo que "b2.buzinar()"

print(b2)

