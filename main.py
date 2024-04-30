from youtube_transcript_api import YouTubeTranscriptApi 
from youtube_transcript_api.formatters import SRTFormatter
import re
import time
from g4f.client import Client
from g4f.Provider import OpenaiChat

from pytube import YouTube

formater = SRTFormatter()

url = "https://www.youtube.com/watch?v=RejZhH-Dfjs&ab_channel=FlowPodcast"
titulo_video = YouTube(url).title
# url = url.replace("-", "")
video_id = re.search(r"v=(\w+-\w+)", url).group(1)
# video_id = video_id.replace("&", "")
print(video_id)

srt = YouTubeTranscriptApi.get_transcript(video_id, languages=['pt'])

srt = formater.format_transcript(srt)

srt = srt.split("\n")

tamanho_srt = len(srt)
print(tamanho_srt)
fator = 60*15

texto_final = ""

client = Client(provider=OpenaiChat)
for i in range(0, tamanho_srt//fator):
    # print(srt[i*fator:(i+1)*fator])
    # time.sleep(10)

    legenda = str(srt[i*fator:(i+1)*fator])
    print(type(legenda))



    mensagem = "Abaixo está um trecho de legenda de uma entrevista no Podcast. Eu não quero a transcrição. Mas preciso que no script me dê o tema abordado nesse range e os seus respectivos minutos. A saída tem que ter rigorosamente o seguinte formato: [MINUTOS: HH:mm:ss - HH:mm:ss] - [TEMA]:[TITULO]" + legenda
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": mensagem}],)
    print(response.choices[0].message.content)

    texto_final += response.choices[0].message.content + "\n\n"


with open(titulo_video+"resumo.txt", "w") as f:
    f.write(texto_final)