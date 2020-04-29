from flask import Flask, jsonify, session, make_response, render_template, url_for
import requests
import json

token = ''


def getToken():
    r = requests.post('http://127.0.0.1:5000/login', auth=('a', 'b'))
    s = json.loads(r.text)
    # print(s['token'])
    return s['token']


token = getToken()


def getAllMovies():
    movies = requests.get('http://127.0.0.1:5000/movies?token=' + token)
    return json.loads(movies.text)


def getAllAuthors():
    authors = requests.get('http://127.0.0.1:5000/authors?token=' + token)
    return json.loads(authors.text)

#getAllMovies()
#getAllAuthors()

for m in getAllMovies():
    print(m['name'])

for m in getAllAuthors():
    print(m['name'])