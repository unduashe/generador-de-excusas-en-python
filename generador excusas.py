import random

excusas = {
    "formal": {
        "disculpa": ("Mis más sinceras disculpas, pero ", "Ruego me discuple, pero ", "Mis más sentidas disculpas, pero"),
         "excusa": ("me ha resultado imposible conseguir lo solicitado, me comprometo a lograrlo lo antes posible", "mi perro se comió los deberes, estoy trabajando en ello para que, con la mayor presteza posible, vuelva a tenerlos disponibles")
    },
    "neutro":{
        "disculpa": ("Hubo un imprevisto, ", "Ha surgido un contratimepo, "),
        "excusa": ("y no he podido hacer lo solicitado, continuo trabajando en ello, perdón", "mi familiar se ha caido y se encuentra hospitalizado, por lo que no he disponido del tiempo suficiente que dedicarle a esto, perdón")
    },
    "informal":{
        "disculpa": ("Por las barbas de barrabás, no te lo creerás, ", "No pude hacer nada", "Mira que lo he intentado, "),
         "excusa": ("pero me he cagado encima asique no está hecho", "pero no solo se comió el ejercicio en el que he trabajado, tambien decidió viajar hasta Francia para comer croisants")
    }
}

def random_num(tipo_registro, cuerpo):
    return random.randint(0, len(excusas[tipo_registro][cuerpo])-1)

def generador_excusas(tipo_registro):
    if tipo_registro not in excusas:
        return print("El tipo de registro introducido no es válido, por favor, indique un registro entre los tres disponibles: formal, neutro, informal")
    resultado = ""
    resultado += excusas[tipo_registro]["disculpa"][random_num(tipo_registro, "disculpa")]
    resultado += excusas[tipo_registro]["excusa"][random_num(tipo_registro, "excusa")]
    return resultado

print(generador_excusas("formal"))