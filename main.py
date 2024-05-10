from youtube_transcript_api import YouTubeTranscriptApi 
from youtube_transcript_api.formatters import SRTFormatter
import re
import time
from g4f.client import Client
from g4f.Provider import OpenaiChat
import json
from json import JSONEncoder
from pytube import YouTube
from pprint import pprint
from menu_template import menu_template
import os
formater = SRTFormatter()

print("\n##### GPT VIDEO RESUMER #####\n")

itens_menu_template = list(menu_template.keys())

print("")
for i in range(len(itens_menu_template)):
    print(str(i) + " - " + itens_menu_template[i])

selecao_menu = int(input("Selecione o tipo de video que voce deseja resumir:"))

msg_template = menu_template[itens_menu_template[selecao_menu]]


url = input("Digite a URL do video: ")
titulo_video = YouTube(url).title
video_id = re.search(r"v=(.+&)", url).group(1)
video_id = video_id.replace("&", "")
print(video_id)

srt = YouTubeTranscriptApi.get_transcript(video_id, languages=['pt'])


srt = formater.format_transcript(srt)

srt = srt.split("\n")

tamanho_srt = len(srt)
print(tamanho_srt)
fator = 60*10

texto_final = ""
texto_json = ""
indice_template = 0



with open("AI_RESUMO"+titulo_video+".json", "w") as f:
    f.write('[\n {"Titulo Video":'  +str(titulo_video)+ ',\n},')

client = Client(provider=OpenaiChat)
for i in range(0, tamanho_srt//fator):
    # print(srt[i*fator:(i+1)*fator])
    # time.sleep(10)
    try:
        legenda = str(srt[i*fator:(i+1)*fator])


        # mensagem = "Abaixo está um trecho de legenda de uma entrevista no Podcast. Eu não quero a transcrição. Mas preciso que no script me dê o tema abordado nesse range e os seus respectivos minutos. A saída tem que ter rigorosamente o seguinte formato: [MINUTOS: HH:mm:ss - HH:mm:ss] - [TEMA]:[TITULO]" + legenda
        mensagem = msg_template + legenda
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": mensagem}],)
        texto_gerado = response.choices[0].message.content
        pprint(texto_gerado)
        texto_final = texto_gerado + ',\n'
    except:
        print("erro")

    with open("AI_RESUMO"+titulo_video+".json", "a") as f:
        f.write(texto_final)    



with open("AI_RESUMO"+titulo_video+".json", "r") as f:
    texto = f.read()
    texto = texto[:-2]
    texto = texto + "]"

with open("AI_RESUMO"+titulo_video+".json", "w") as f:
    f.write(texto)



with open("ROTEIRO "+titulo_video+".md", "w") as f:
    cmd = "Você é um roterista profissional. Que tem um linguajar moderno e de boa escrita e de forma criativa. Preciso que crie um roteiro para um video no youtube explicando, detalhando e aumentando o conteudo com pensamentos filosoficos, sociologicos e psicologicos contido no resumo do filme que esta no arquivo JSON abaixo. Durante a fala do narrador também incluir trechos do conteudo do resumo. \n"
    response = client.chat.completions.create(
        model="gpt-4-gizmo",
        messages=[{"role": "user", "content": cmd + texto}],
    )

    f.write(response.choices[0].message.content)    