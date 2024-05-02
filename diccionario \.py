meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma" ,
            "SHEESH": "ligera desaprobación" , 
            "AGGRO": "ponerse agresivo/enojado",
            "GG": "buen juego o en ingles Good Game",
            "IDK": "yo no se o en ingles I Don't Know"
            }
            
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('Desculpa en este momento no lo tenemos en nuestro diccionario')
  
