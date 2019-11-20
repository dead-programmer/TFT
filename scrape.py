''' Lines 2-28 were taken from:
https://stackoverflow.com/questions/37754138/how-to-render-html-with-pyqt5s-qwebengineview
'''
def render(url):
    """Fully render HTML, JavaScript and all."""

    import sys
    from PyQt5.QtCore import QEventLoop,QUrl
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtWebEngineWidgets import QWebEngineView

    class Render(QWebEngineView):
        def __init__(self, url):
            self.html = None
            self.app = QApplication(sys.argv)
            QWebEngineView.__init__(self)
            self.loadFinished.connect(self._loadFinished)
            self.load(QUrl(url))
            while self.html is None:
                self.app.processEvents(QEventLoop.ExcludeUserInputEvents | QEventLoop.ExcludeSocketNotifiers | QEventLoop.WaitForMoreEvents)
            self.app.quit()

        def _callable(self, data):
            self.html = data
            self.app.quit()

        def _loadFinished(self, result):
            self.page().toHtml(self._callable)

    return Render(url).html


import requests
from bs4 import BeautifulSoup

url = "https://tftactics.gg/tierlist/team-comps/"
html = requests.get(url).text
renderedHTML = render(url)
soup = BeautifulSoup(renderedHTML,"html.parser")
#Returns a list of all the team characters (use their hrefs to parse the names)
teamCharacters = soup.find_all(class_="team-characters")
preScrapeTeamNames = soup.find_all('div',{"class" : "team-name"})
teamList = []
tierList = []
for each in preScrapeTeamNames:
    name = each.text
    tier = name[:1]
    if tier != 'S' and tier != 'A':
        continue
    tierList.append(tier)
    newName = name[1:]
    teamList.append(newName)
numOfTeamCharactersNeeded = len(teamList)
preScrapeTeamCharactersAll = soup.find_all('div',{"class" : "team-characters"})
preScrapeTeamCharactersStoA = preScrapeTeamCharactersAll[:numOfTeamCharactersNeeded]

#a = soup.find_all(class_="characters-list")
#work witht his to get the a class and href from that a class
''' possible solution
for a in preScrapeTeamCharactersStoA:
    for i in  a.find_all('img', alt=True):
        c = i['src']
        print(c)


for j in b:                                         
    c = j.find_all("div",{"class":"team-portrait"})
    for k in c:
        d = k.find("div",{"class":"team-characters"})
        print(d)

'''
a = soup.find_all("div",{"class" : "tier-group"})
empty_list = []
for i in range(0,2):
    b = a[i].find_all("div",{"class":"characters-list"})
    for j in b:
        c = j.find_all("div",{"class":"team-portrait"})
        for k in c:
            d = k.find("div",{"class":"team-characters"})
            for q in d:
                y = d.find_all('a', href=True)
                team = [] 
                for p in y:      
                    team.append(p["href"])
                empty_list.append(team)

#problem is theres is 102 elements in the empty_list but there should only be 13?