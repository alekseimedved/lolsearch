from flask import Flask, request, render_template
import requests
import json
from flask import jsonify


app = Flask(__name__)
RGAPI = ''  # your api goes here

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html'
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/a1', methods=['GET'])
def a1():
    url = "https://euw1.api.riotgames.com/lol/status/v4/platform-data"
    payload={}
    headers = {
      'X-Riot-Token': RGAPI
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return(response.text)

@app.route('/getSummoner/<username>', methods=['GET'])
def getSummoner(username):
    url = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + username
    payload={}
    headers = {
      'X-Riot-Token': RGAPI
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return(response.text)

@app.route('/getRank/<summonerId>', methods=['GET'])
def getRank(summonerId):
    url = "https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + summonerId
    payload={}
    headers = {
      'X-Riot-Token': RGAPI
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return(response.text)

@app.route('/getChampions/<summonerId>', methods=['GET'])
def getChampions(summonerId):
    url = "https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + summonerId
    payload={}
    headers = {
      'X-Riot-Token': RGAPI
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return(response.text)

@app.route('/getLastMatches/<puuId>/<c>', methods=['GET'])
def getLastMatches(puuId, c):
    url = "https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/" + puuId +"/ids?start=0&count=" + c
    payload={}
    headers = {
      'X-Riot-Token': RGAPI
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return(response.text)

@app.route('/getMatchData/<matchId>', methods=['GET'])
def getMatchData(matchId):
    url = "https://europe.api.riotgames.com/lol/match/v5/matches/" + matchId
    
    payload={}
    headers = {
      'X-Riot-Token': RGAPI
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return(response.text)


@app.route('/test', methods=['GET'])
def test():
    xd = {
        'data': 1
    }
    return(xd)

if __name__ == '__main__':
    app.run(debug=True)