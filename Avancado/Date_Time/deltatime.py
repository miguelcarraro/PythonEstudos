from datetime import datetime, timedelta, date

tipo_carro = input("Qual o tamanho do Carro? ")
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f'O carro chegou: {data_atual} e ficara pronto às: {data_estimada}')

elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f'O carro chegou: {data_atual} e ficara pronto às: {data_estimada}')
    

else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f'O carro chegou: {data_atual} e ficara pronto às: {data_estimada}')
    
print(date.today() - timedelta(weeks=1)) # Decrementando valor de datas.