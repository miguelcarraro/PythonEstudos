class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}:{','.join([f'{chave}={valor}'for chave, valor in self.__dict__.items()])}"

        

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)
        

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)
        

class Cachorro(Mamifero):
    def __str__(self):
        return "Cachorro"

class Gato(Mamifero):
    def __str__(self):
        return "Gato"


class Leao(Mamifero):
    def __str__(self):
        return "Leão"

class Ornitorrinco(Mamifero, Ave):
    def __str__(self):
        return "Ornitorrinco"

gato = Gato(nro_patas=4, cor_pelo="Preto")
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="amarelo")
print(ornitorrinco)

leao = Leao(nro_patas=4, cor_pelo="amarelo")
print(leao)

cachorro = Cachorro(nro_patas=4, cor_pelo="preto")
print(cachorro)