#srtftime formata o valor 
#strptime transformar um valor string em um valor trabalhavel para o "time"

from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2025-03-14 20:35"
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)

