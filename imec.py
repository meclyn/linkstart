import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
from get_env import print_env

import openai  

env = print_env(['app_key'])

#configura o ambiente
openai.api_key = env['app_key']

model_engine = 'gpt-3.5-turbo'

audio = sr.Recognizer()
maquina = pyttsx3.init()

def listen_command():
    comando = ""  # Inicializa a variável
    try:
        with sr.Microphone() as source:
            print('Escutando...')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'link' in comando:
                comando = comando.replace('link', '')
                maquina.say(comando)
                maquina.runAndWait()
        
    except Exception as e:
        print(f'Um erro inesperado aconteceu: {e}')
    return comando

def execute_command():
    comando = listen_command()
    if 'sair' in comando:  # Comando para sair
        print("Encerrando o assistente.")
        maquina.say("Encerrando o assistente.")
        maquina.runAndWait()
        return False  # Para sair do loop
    if 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar, 2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'toque' in comando:
        musica = comando.replace('toque','')
        resultado = pywhatkit.playonyt(musica)
        maquina.say(f'Tocando {musica} no youtube')
        maquina.runAndWait()

    elif 'responda' in comando or 'fale sobre' in comando or 'crie' in comando or 'o que você acha sobre' in comando:
        prompt = comando.replace('responda','')
        completion = openai.completions.create(
            model = model_engine,
            prompt = prompt,
            max_tokens = 1024,
            temperature = 0.5,
        )
        reponse = completion.choices[0].text
        print(reponse)
        maquina.say(reponse)
        maquina.runAndWait()

while True:
    execute_command()
    saida = input('Deseja sair?')
    if saida == 'sim':
        break
