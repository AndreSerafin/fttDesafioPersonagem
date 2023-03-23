from flask import Flask
from flask_restx import Api, Resource

from src.server.instance import server

app, api = server.app, server.api

characters_db = [
    {'id': 0, 'name': 'Ben 10', 'description': 'menino que se transforma em alien', 'link': 'htttps://www.linkplaceholder.com', 'program': 'programa aleatorio', 'animador' : 'cartoon network'},
    {'id': 1, 'name': 'Pokemon', 'description': 'criaturas com habilidades especiais', 'link': 'https://www.linkplaceholder.com', 'program': 'anime famoso', 'animador': 'TV Tokyo'},
    {'id': 2, 'name': 'Tom e Jerry', 'description': 'gato e rato em eterna rivalidade', 'link': 'https://www.linkplaceholder.com', 'program': 'desenho animado classico', 'animador': 'Metro-Goldwyn-Mayer'},
    {'id': 3, 'name': 'Os Simpsons', 'description': 'familia disfuncional e suas aventuras', 'link': 'https://www.linkplaceholder.com', 'program': 'serie de animacao adulta', 'animador': 'Fox Broadcasting Company'},
    {'id': 4, 'name': 'Hora de Aventura', 'description': 'aventuras de Finn e Jake no mundo de Ooo', 'link': 'https://www.linkplaceholder.com', 'program': 'desenho animado de fantasia', 'animador': 'Cartoon Network Studios'},
]

@api.route('/characters')
class CharactersList(Resource):
    def get(self, ):
        return characters_db
    
    def post(self, ):
        response = (api.payload)
        characters_db.append(response)
        return response, 200