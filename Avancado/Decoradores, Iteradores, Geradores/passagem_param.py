def mensagem(nome):
    print("executando nome")
    return f"Oi {nome}"

def mensagem_longa(nome):
    print("executando mensagem longa")
    return f"Ola tudo bem com você {nome}"

def executar(funcao, nome):
    print("Executando")
    return funcao(nome)

print(executar(mensagem,"Miguel"))
print(executar(mensagem_longa, "Miguel"))