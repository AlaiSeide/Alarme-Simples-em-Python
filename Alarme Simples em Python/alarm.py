import datetime
import time
import playsound

# Solicita ao usuário que digite o horário do alarme
horario_alarme = input("Digite o horário do alarme (HH:MM:SS): ")
hora_alarme = horario_alarme.split(":")[0]
minuto_alarme = horario_alarme.split(":")[1]

while True:
    agora = datetime.datetime.now()
    hora_atual = agora.hour
    minuto_atual = agora.minute

    # Verifica se o horário atual é igual ao horário do alarme
    if hora_atual == int(hora_alarme) and minuto_atual == int(minuto_alarme):
        print("Alarme disparado!")
        playsound.playsound("music/music.mp3")  # Substitua "music/music.mp3" pelo caminho real do seu arquivo de áudio
        break

    time.sleep(1)
