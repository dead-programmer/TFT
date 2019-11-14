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
for each in preScrapeTeamNames:
    name = each.text
    tier = name[:1]
    if tier != 'S' and tier != 'A':
        continue
    newName = name[1:]
    teamList.append(newName)

numOfTeamCharactersNeeded = len(teamList)
preScrapeTeamCharactersAll = soup.find_all('div',{"class" : "team-characters"})
preScrapeTeamCharactersStoA = preScrapeTeamCharactersAll[:numOfTeamCharactersNeeded]

#work witht his to get the a class and href from that a class