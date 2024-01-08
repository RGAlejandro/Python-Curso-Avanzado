import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# escuchar nuestro microfono y devolver el audio como texto
def transformar_audio_en_texto():
    #almacenar recognizer en variable
    r = sr.Recognizer()

    #configurar el microfono
    with sr.Microphone() as origen:

        #tiempo de espera
        r.pause_threshold = 0.8

        print("Ya puedes hablar")

        #informar que comenzo la grabacion
        audio = r.listen(origen)

        try:
            #buscar en Google
            pedido = r.recognize_google(audio, language="es-es")

            print("Dijiste: "+ pedido)
            return pedido

        except sr.UnknownValueError:

            #prueba de que no comprendio el audio
            print("ups no entendi")

            return "sigo esperando"
        except sr.RequestError:
            # prueba de que no comprendio el audio
            print("ups no hay servicio")

            return "sigo esperando"
        except:
            # prueba de que no comprendio el audio
            print("ups algo ha salido mal")

            return "sigo esperando"
#opciones de voz/idiona
#id1 ="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"

#id2 ="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
#transformar_audio_en_texto() no funciona
def hablar(mensaje):
    #encender el motor pyttsx3
    engine = pyttsx3.init()
    """
    for voz in engine.getProperty("voices"):
        print(voz)
    """

    #pronuncar mensaje
    engine.say(mensaje)
    engine.runAndWait()


def pedir_dia():
    #crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    dia_semana = dia.weekday()
    print(dia_semana)

    #diccionario con nombre de dias
    calendario = {
    0:"Lunes", 1:"Martes", 2:"Miércoles", 3:"Jueves", 4:"Viernes", 5:"Sábado", 6:"Domingo",
    }

    # decir el dia de la semana
    hablar(f"Hoy es {calendario[dia_semana]}")

def pedir_hora():
    #crear variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f"En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos"
    print(hora)

    #decir la hora
    hablar(hora)

def saludo_inicial():

    #crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches"
    elif 6 <= hora.hour < 13:
        momento ="Buen dia"
    else:
        momento = "Buenas tardes"
    #decir el saludo

    hablar(f"{momento}, soy Helena, tu asistente personal, Por favor, dime en que te puedo ayudar")


#funcion central del asistente
def pedir_cosas():
     #activar saludo inicial
     saludo_inicial()

     comenzar = True

     while comenzar:
         pedido = transformar_audio_en_texto().lower()

         if "abrir youtube" in pedido:
             hablar("Con gusto, estoy abriendo YouTube")
             webbrowser.open("https_//www.youtube.com")
             continue
         elif "abrir navegador" in pedido:
             hablar("Con gusto, estoy abriendo Google")
             webbrowser.open("https_//www.google.com")
             continue
         elif "que dia es hoy" in pedido:
             pedir_dia()
             continue
         elif "que hora es" in pedido:
             pedir_hora()
             continue
         elif "buscar en wikipedia" in pedido:
             hablar("Buscando en wikipedia")
             pedido = pedido.replace("Busca en wikipedia","")
             wikipedia.set_lang("es")
             resultado = wikipedia.summary(pedido, sentences=1)
             hablar("wikipedia dice lo siguiente: ")
             hablar(resultado)
             continue
         elif "busca en internet" in pedido:
             hablar("Ya mismo estoy en eso")
             pedido = pedido.replace("busca en internet", "")
             pywhatkit.search(pedido)
             hablar("Esto es lo que he encontrado")
             continue
         elif "reproducir" in pedido:
             hablar("Buena idea, ya comienzo a reproducirlo")
             pywhatkit.playonyt(pedido)
             continue
         elif "broma" in pedido:
             hablar(pyjokes.get_joke("es"))
             continue
         elif "precio de las acciones" in pedido:
             accion = pedido.split("de")[-1].strip()
             cartera = {"apple":"APPL","amazon":"AMZN","google":"GOOGL"}
             try:
                 accion_buscada = cartera[accion]
                 accion_buscada = yf.Ticker(accion_buscada)
                 precio_actual = accion_buscada.info["regularMarketPrice"]
                 hablar(f"La encontré, el precio de {accion} es {precio_actual}")
                 continue
             except:
                 hablar("Perdón pero no la he encontrado")
                 continue
         elif "adiós" in pedido:
             hablar("Me voy a descansar, cualquier cosa me avisas")
             break
#hablar("Hola Alejandro, espero que tengas un buen día")

#pedir_dia()
#pedir_hora()
#saludo_inicial()
pedir_cosas()