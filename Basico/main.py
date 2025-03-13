pessoa = {"1": "Bola de fogo", "2": "Raio do trovão", "3": "Flechada de cu"}




while True:

    escolha = input('''

    Escolha a sua magia: 
1 - Bola de fogo
2 - Raio do trovão
3 - Flechada de cu

''')


    if escolha in pessoa:
        print("A magia é\n" , pessoa[escolha])

