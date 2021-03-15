# -*- coding: utf-8 -*-

import speech_recognition as speech
import pyttsx3
import pywhatkit
import datetime as time
import wikipedia
import chistesESP as chistes
import random

# Nombre del asistente
name='nombre'# TODO: Debes ingresar el nombre de tu asistente aqui

# Permite reconocer la voz
listener = speech.Recognizer()

engine = pyttsx3.init()

"""RATE DEL ASISTENTE"""
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

"""VOZ DEL ASISTENTE"""
voice_engine = engine.getProperty('voices')
engine.setProperty('voice', voice_engine[0].id)

"""LENGUAJE DE WIKIPEDIA"""
wikipedia.set_lang('es')

# Traduccion de los meses
spanish_month = {
    'January': 'Enero',
    'February': 'Febrero',
    'March': 'Marzo',
    'April': 'Abril',
    'May': 'Mayo',
    'June': 'Junio',
    'July': 'Julio',
    'August': 'Agosto',
    'September': 'Septiembre',
    'October': 'Octubre',
    'November': 'Noviembre',
    'December': 'Diciembre'
}

# Selecciona una palabra de forma aleatoria
def random_choice():
    lista = ['Te escucho', 'Dime tu orden', 'Estoy escuchándote', 'Dime']
    seleccion = random.choice(lista)
    return seleccion

# Meotodo que permite al asistente hablar
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Metodo que permite al asuste escuchar
def listen():
    try:
        with speech.Microphone() as source:
            select = random_choice()
            print('Escuchando...')
            talk(select)
            voice = listener.listen(source)
            recognizer = listener.recognize_google(voice, language='es-MX')
            recognizer = recognizer.lower()

            if name in recognizer:
                recognizer = recognizer.replace(name, '')
    except:
        print('Algo ha salido mal')
        pass
    return recognizer

# Metodo que ejecuta al asistente
def run():
    recognizer = listen()

    print(recognizer)

    # REPRODUCE UN VIDEO EN YOUTUBE
    if 'reproduce' in recognizer:
        music = recognizer.replace('reproduce', '')
        talk('reproduciendo' + music)
        pywhatkit.playonyt(music)

    # INDICA LA HORA ACTUAL
    elif 'hora' in recognizer:
        hora = time.datetime.now().strftime('%I:y%M %p')
        talk('Son las '+hora)

    # INDICA EL DIA MES Y AÑO
    elif 'fecha' in recognizer:
        fecha = time.datetime.now().strftime('%d-%h-%Y')
        talk('La fecha es: ' + str(fecha))

    # INDICA EL DIA
    elif 'día' in recognizer:
        dia = time.datetime.now().strftime('%d')
        talk('Hoy es el día ' + str(dia))

    # INDICA EL MES
    elif 'mes' in recognizer:
        mes = time.datetime.now().strftime('%B')
        mes_translate = spanish_month[mes]
        talk('Estamos en el mes de ' + str(mes_translate))

    # INDICA EL AÑO
    elif 'año' in recognizer:
        year = time.datetime.now().strftime('%Y')
        talk('Estamos en el ' + str(year))

    # BUSCA EN WIKIPEDIA
    elif 'busca en wikipedia' in recognizer:
        consulta = recognizer.replace('busca en wikipedia', '')
        talk('buscando en wikipedia' + consulta)
        resultado = wikipedia.summary(consulta, sentences=3)
        talk(resultado)

    # BUSCA EN GOOGLE
    elif 'busca en google' in recognizer:
        consulta = recognizer.replace('busca en google', '')
        talk('Buscando en google' + consulta)
        pywhatkit.search(consulta)

    # CHISTES
    elif 'chiste' in recognizer:
        chiste = chistes.get_random_chiste()
        talk(chiste)

    else:
        talk('Disculpa, no te entiendo')
