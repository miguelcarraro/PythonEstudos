def principal():
    print("executando a função principal")

    def funcao_interna():
        print("executando a primeira função interna")

    def funcao_2():
        print("executando segunda função interna")

    funcao_interna()
    funcao_2()

principal()