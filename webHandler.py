from urllib import request
import LogicHandler
import json
import webbrowser
LogicHandler.indicateLoading("Loading " + __name__)

def getLatestVersion():
    req = request.Request('https://api.github.com/repos/NuclideK/MooCalc/releases/latest', headers={'Accept': 'application/vnd.github.v3+json'})
    data = json.loads(request.urlopen(req).read().decode('utf-8'))
    return data

def openWebsite(url: str):
    webbrowser.open(url)

LogicHandler.indicateSuccess(f"{__name__} loaded [S]")
