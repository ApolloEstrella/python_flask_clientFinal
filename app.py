from flask import Flask, jsonify, session, make_response, render_template, url_for
import requests
import json

token = ''

def getToken(): 
    r = requests.post('http://127.0.0.1:5000/login', auth=('a', 'b')) 
    s = json.loads(r.text)
    #print(s['token'])
    return s['token']

token = getToken()   
 

def getAuth():
    s = requests.get('http://127.0.0.1:5000/auth?token=' + token) 
    return



getAuth()   