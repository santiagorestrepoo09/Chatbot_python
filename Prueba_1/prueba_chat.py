from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

import re
import random

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

        response('BIENVENIDO A MCT', ['hola', 'klk', 'saludos', 'buenas'], single_response = True)
        response('¿En que te puedo ayudar?', ['como', 'estas', 'va', 'vas', 'sientes'], required_words=['como'])
        response('Se programar en pyhton', ['sabes', 'tu', 'conoces' , 'programar' , 'programacion'], single_response=True)
        response('Si, y ¿ tu sabes programar?', ['bueno', 'chevere', 'que' , 'super' , 'fabuloso'], single_response=True)
        response('En que lenguaje', ['si', 'claro', 'porsupuesto' , 'un poco' , 'maso menos '], single_response=True)
        response('Estamos ubicados en la calle 23 numero 123', ['ubicados', 'direccion', 'donde', 'ubicacion'], single_response=True)
        response('Siempre a la orden', ['gracias', 'te lo agradezco', 'thanks'], single_response=True)

        best_match = max(highest_prob, key=highest_prob.get)
        #print(highest_prob)

        return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'búscalo en google a ver que tal'][random.randrange(3)]
    return response

while True:
    print("Bot: " + get_response(input('You: ')))