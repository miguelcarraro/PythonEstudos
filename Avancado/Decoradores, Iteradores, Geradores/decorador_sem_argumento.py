def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar")
        funcao()
        print("Algo depois de executar")

    return envelope

@meu_decorador
def ola_mundo():
    print("Ola mundo!")
    

# ola_mundo = meu_decorador(ola_mundo) - Sem decoradores "@" preciso declarar o uso da função
ola_mundo()